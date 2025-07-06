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
#DirectoryListener will handle printing and sending to poison queue, you only need to throw the KnownProcessingException
#Any known exception messages should be short and to the point, as they will be sent to results
#TODO: We may want to add a way to send more detailed information to a log file, low priority
def processExperiment(experimentId: str, fileName: str, videoNumber: int):
    print("Processing experiment: " + experimentId)
    videoNumber = int(videoNumber)

    #Get data
    experiment: Experiment
    try:
        experiment = ExperimentApi(appSettings.ExperimentsEndpoint, tokenManager).getExperimentById(experimentId)
    except Exception as e:
        raise Exception("Failed to get experiment data for " + experimentId + ": " + str(e))

    # Run the video through the network
    # sequence_item: SequenceItem = next((obj for obj in experiment.Sequences if obj.SequenceId == int(videoNumber)), None)
    for sequence in experiment.Sequences:
        if sequence.SequenceId == int(videoNumber):
            sequence_item: SequenceItem = sequence

    if sequence_item is None:
        raise Exception("Failed to get sequence item for " + experimentId + ": " + str(experiment))

    # Get the network configuration from the Infrastructure API
    try:
        network: Network = InfrastructureApi(appSettings.InfrastructureEndpoint, tokenManager).getNetworkProfileById(str(sequence_item.NetworkTopologyId))
    except Exception as e:
        raise Exception("Failed to get network profile for " + experimentId + ": " + str(e))

    net_emulator: NetworkEmulator = NetworkEmulator(sequence_item, experiment, network, f"{fileName}")
    disrupted_file, streaming_log = net_emulator.run()
    print(f"Video {fileName} streaming completed")
    # Run through network
    bitrate = MetricEvaluator.evaluateBitRate(streaming_log) # Bitrate metric is gathered at streaming stage
    print(f"Bitrate extracted")

    # Get metrics
    videoMetricValues = MetricEvaluator.evaluate(f"{appSettings.VideoRevieverTargetFolder}/{fileName}", disrupted_file)
    # videoResults: VideoResultMetrics = VideoResultMetrics(bitrate, videoMetricValues.index(0), videoMetricValues.index(1), videoMetricValues.index(2))
    videoResults: VideoResultMetrics = VideoResultMetrics(bitrate, videoMetricValues[0], videoMetricValues[1], videoMetricValues[2])

    # corrospondingExperiment: SequenceItem = experiment.Sequences[int(videoNumber)]
    corrospondingExperiment: SequenceItem = next((obj for obj in experiment.Sequences if obj.SequenceId == int(videoNumber)), None)
    videoResultSetItem: ResultSetItem = ResultSetItem(SequenceID=corrospondingExperiment.SequenceId, NetworkTopologyId=corrospondingExperiment.NetworkTopologyId,DistruptionProfileId= corrospondingExperiment.NetworkDisruptionProfileId,EncodingParameters=corrospondingExperiment.EncodingParameters, Results=videoResults)

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
