from exceptions.KnownProcessingException import KnownProcessingException
from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, GenericResponse, ResultSet
from AppSettings import AppSettings, GetAppSettings
from network_emulation.NetworkEmulation import NetworkEmulator
import os
import time
from processing.DirectoryListener import DirectoryListener

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
    try:
        experiment: Experiment = ExperimentApi(appSettings.ExperimentsEndpoint).getExperimentById(experimentId)
    except Exception as e:
        raise Exception("Failed to get experiment data for " + experimentId + ": " + str(e))

    # Run each of the videos in the experiment through the network
    for experimentItem in experiment.Set:
        net_emulator: NetworkEmulator = NetworkEmulator(experimentItem, experiment)
        net_emulator.run()

    #Get metrics

    #Send result
    try:
        resultResponse: GenericResponse = ResultApi(appSettings.ResultsEndpoint).sendResults(experimentId, ResultSet("Test"))
    except Exception as e:
        raise KnownProcessingException(experimentId, "Failed to send results", experiment.ownerId, experiment.partner)

    print("Everything ran!")
    print("ExperimentId: " + experiment.id)
    print("ResultResponseMessage: " + resultResponse.message)

# Injected function to send errors to results
def handleKnownProcessingException(exception: KnownProcessingException):
    ResultApi(appSettings.ResultsEndpoint).sendError(exception.experimentId, exception.message, exception.ownerId, exception.partner)

#Start listening
listener: DirectoryListener = DirectoryListener(appSettings.ListenerTargetFolder, ["README.md"], processExperiment, handleKnownProcessingException)
listener.start()
