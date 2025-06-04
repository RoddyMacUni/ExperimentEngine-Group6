from exceptions.KnownProcessingException import KnownProcessingException
from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, GenericResponse, ResultSet
from AppSettings import AppSettings, GetAppSettings
import os
import time
from processing.DirectoryListener import DirectoryListener

EndTaskFlag: bool = False

appSettings: AppSettings = GetAppSettings()

#Any exception in here that can pass ANY information to results should be a KnownProcessingException
#This will include ALL exceptions after the experiment API call
#IMPORTANT: DirectoryListener will handle printing and sending to poision queue, you only need to throw the KnownProcessingException
def processExperiment(fileName: str, experimentId: str, videoNumber: int):
    print("Processing experiment: " + experimentId)
    #Get data
    experiment: Experiment = ExperimentApi(appSettings.ExperimentsEndpoint).getExperimentById(experimentId)

    #Run through network

    #Get metrics

    #Send result
    resultResponse: GenericResponse = ResultApi(appSettings.ResultsEndpoint).sendResults(experimentId, ResultSet("Test"))

    print("Everything ran!")
    print("ExperimentId: " + experiment.id)
    print("ResultResponseMessage: " + resultResponse.message)

# Injected function to send errors to results
def handleKnownProcessingException(exception: KnownProcessingException):
    ResultApi(appSettings.ResultsEndpoint).sendError(exception.experimentId, exception.message, exception.ownerId, exception.partner)

#Start listening
listener: DirectoryListener = DirectoryListener(appSettings.ListenerTargetFolder, ["README.md"], processExperiment, handleKnownProcessingException)
listener.start()
