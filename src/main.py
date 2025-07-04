from exceptions.KnownProcessingException import KnownProcessingException
from api.ExperimentApi import ExperimentApi, Experiment
from api.InfrastructureApi import InfrastructureApi
from api.ResultApi import ResultApi, GenericResponse
from AppSettings import AppSettings, GetAppSettings
from network_emulation.NetworkEmulation import NetworkEmulator
from model.Network import Network
from processing.DirectoryListener import DirectoryListener
from model.ResultSet import ResultSet, VideoResultMetrics, ResultSetItem
from model.Experiment import SequenceItem
from processing.ResultCompiler import ResultCompiler
from api.TokenManager import TokenManager
from video_metrics.Metric import MetricEvaluator

EndTaskFlag: bool = False

appSettings: AppSettings = GetAppSettings()
tokenManager: TokenManager = TokenManager(appSettings.AuthEndpoint)

#IMPORTANT
#Any exception in here that can pass ANY information to results should be a KnownProcessingException
#This will include ALL exceptions after the experiment API call
#DirectoryListener will handle printing and sending to poision queue, you only need to throw the KnownProcessingException
#Any known exception messages should be short and to the point, as they will be sent to results
#TODO: We may want to add a way to send more detailed information to a log file, low priority
def processExperiment(experimentId: str, fileName: str, videoNumber: int):
    print("Processing experiment: " + experimentId)

    #Get data
    experiment: Experiment
    try:
        experiment = ExperimentApi(appSettings.ExperimentsEndpoint, tokenManager).getExperimentById(experimentId)
    except Exception as e:
        raise Exception("Failed to get experiment data for " + experimentId + ": " + str(e))

    # Run the video through the network
    sequence_item: SequenceItem = experiment.Sequences[videoNumber]
    net: Network = InfrastructureApi.getNetworkProfileById(str(sequence_item.NetworkTopologyId))
    net_emulator: NetworkEmulator = NetworkEmulator(sequence_item, experiment, net, fileName)
    disrupted_file, streaming_log = net_emulator.run()

    # Run through network
    bitrate = MetricEvaluator.evaluateBitRate(streaming_log) # Bitrate metric is gathered at streaming stage

    # Get metrics
    videoMetricValues = MetricEvaluator.evaluate(fileName, disrupted_file) #TODO: Change second param to saved degraded video file, just keep it as sample for now
    videoResults: VideoResultMetrics = VideoResultMetrics(bitrate, videoMetricValues.index(0), videoMetricValues.index(1), videoMetricValues.index(2))

    corrospondingExperiment: SequenceItem = experiment.Sequences[int(videoNumber)]
    videoResultSetItem: ResultSetItem = ResultSetItem(corrospondingExperiment.EncodingParameters, int(videoNumber), corrospondingExperiment.NetworkTopologyId, corrospondingExperiment.NetworkDisruptionProfileId, videoResults) #TODO create constructor here

    #Build partial result file
    partialResultsFile: ResultSet = ResultSet(None, experiment.Id, experiment.OwnerId, [videoResultSetItem])
    
    #Compile full result file or save next step of partial results file 
    finalResultsFile: ResultSet | None = ResultCompiler().CompileResultsFile(partialResultsFile, experiment) #TODO: if this errors, it should delete corrosponding saved files

    #If partial results file is not complete, start next loop
    if finalResultsFile is None:
        return  
    
    #Otherwise, send results
    try:
        resultResponse: GenericResponse = ResultApi(appSettings.ResultsEndpoint, tokenManager).sendResults(experimentId, finalResultsFile)
    except Exception as e:
        raise KnownProcessingException(experimentId, "Failed to send results", experiment.OwnerId)

# Injected function to send errors to results
def handleKnownProcessingException(exception: KnownProcessingException):
    ResultApi(appSettings.ResultsEndpoint, tokenManager).sendError(exception.experimentId, exception.message, exception.ownerId)

if __name__ == "__main__":
    #Start listening
    listener: DirectoryListener = DirectoryListener(appSettings.ListenerTargetFolder, ["README.md"], processExperiment, handleKnownProcessingException)
    listener.start()
