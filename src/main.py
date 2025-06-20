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

    #Run through network

    #Get metrics
    videoResults: VideoResultMetrics = VideoResultMetrics(100, 100, 100, 100) #TODO: implement

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

#Start listening
listener: DirectoryListener = DirectoryListener(appSettings.ListenerTargetFolder, ["README.md"], processExperiment, handleKnownProcessingException)
listener.start()
