from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, GenericResponse, ResultSet
from AppSettings import AppSettings, GetAppSettings
import os
import time
from processing.DirectoryListener import DirectoryListener

EndTaskFlag: bool = False

appSettings: AppSettings = GetAppSettings()

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

#Start listening
listener: DirectoryListener = DirectoryListener(appSettings.ListenerTargetFolder, ["README.md"], processExperiment)
listener.start()
