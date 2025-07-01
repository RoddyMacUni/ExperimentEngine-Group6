from exceptions.KnownProcessingException import KnownProcessingException
from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, GenericResponse
from AppSettings import AppSettings, GetAppSettings
import os
import time
from processing.DirectoryListener import DirectoryListener
from model.ResultSet import ResultSet, VideoResultMetrics, ResultSetItem
from model.Experiment import ExperimentSetItem
from processing.ResultCompiler import ResultCompiler
from video_metrics.Metric import MetricEvaluator

EndTaskFlag: bool = False

appSettings: AppSettings = GetAppSettings()

#IMPORTANT
#Any exception in here that can pass ANY information to results should be a KnownProcessingException
#This will include ALL exceptions after the experiment API call
#DirectoryListener will handle printing and sending to poision queue, you only need to throw the KnownProcessingException
#Any known exception messages should be short and to the point, as they will be sent to results
#TODO: We may want to add a way to send more detailed information to a log file, low priority
def processExperiment(fileName: str, experimentId: str, videoNumber: int):
    print("Processing experiment: " + experimentId)
    #Get data
    experiment: Experiment
    try:
        experiment = ExperimentApi(appSettings.ExperimentsEndpoint).getExperimentById(experimentId)
    except Exception as e:
        raise Exception("Failed to get experiment data for " + experimentId + ": " + str(e))

    # Run through network
    bitrate = MetricEvaluator.evaluateBitRate("[out#0/mp4 @ 0x63bf77a99380] video:266KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 1.627007%\nframe=  296 fps= 10 q=-1.0 Lsize=     270KiB time=00:00:09.80 bitrate= 225.8kbits/s dup=0 drop=4 speed=0.334x\n[libx264 @ 0x63bf77a5fc80] frame I:2     Avg QP:21.26  size: 14844") # Bitrate metric is gathered at streaming stage

    # Get metrics
    videoMetricValues = MetricEvaluator.evaluate(fileName, "../../test_videos/sample_degraded.mp4") #TODO: Change second param to saved degraded video file, just keep it as sample for now
    videoResults: VideoResultMetrics = VideoResultMetrics(bitrate, videoMetricValues.index(0), videoMetricValues.index(1), videoMetricValues.index(2))

    corrospondingExperiment: ExperimentSetItem = experiment.Set[int(videoNumber)]
    videoResultSetItem: ResultSetItem = ResultSetItem(corrospondingExperiment.EncodingParameters, int(videoNumber), corrospondingExperiment.NetworkTopologyId, corrospondingExperiment.networkDisruptionProfileId, videoResults) #TODO create constructor here

    #Build partial result file
    partialResultsFile: ResultSet = ResultSet(None, "", int(experiment.id), experiment.OwnerId, [ videoResultSetItem ])
    
    #Compile full result file or save next step of partial results file 
    finalResultsFile: ResultSet | None = ResultCompiler().CompileResultsFile(partialResultsFile, experiment) #TODO: if this errors, it should delete corrosponding saved files

    #If partial results file is not complete, start next loop
    if finalResultsFile is None:
        return  
    
    #Otherwise, send results
    try:
        resultResponse: GenericResponse = ResultApi(appSettings.ResultsEndpoint).sendResults(experimentId, finalResultsFile)
    except Exception as e:
        raise KnownProcessingException(experimentId, "Failed to send results", experiment.ownerId, experiment.partner)

# Injected function to send errors to results
def handleKnownProcessingException(exception: KnownProcessingException):
    ResultApi(appSettings.ResultsEndpoint).sendError(exception.experimentId, exception.message, exception.ownerId, exception.partner)

if __name__ == "__main__":
    #Start listening
    listener: DirectoryListener = DirectoryListener(appSettings.ListenerTargetFolder, ["README.md"], processExperiment, handleKnownProcessingException)
    listener.start()
