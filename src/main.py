from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, GenericResponse, ResultSet
from AppSettings import AppSettings, GetAppSettings
import os
import time
from processing.Counter import Counter

EndTaskFlag: bool = False

appSettings: AppSettings = GetAppSettings()

def processExperiment(experimentId: str):
    #Get data
    experiment: Experiment = ExperimentApi(appSettings.ExperimentsEndpoint).getExperimentById("TODO")

    #Run through network

    #Get metrics

    #Send result
    resultResponse: GenericResponse = ResultApi(appSettings.ResultsEndpoint).sendResults("TODO", ResultSet("Test"))

    print("Everything ran!")
    print("ExperimentId: " + experiment.id)
    print("ResultResponseMessage: " + resultResponse.message)

print("Listening for file on " + appSettings.ListenerTargetFolder)
#Listen for new file
counter = Counter(60, lambda minutes: print("No new file detected for " + str(minutes) + " minutes."))
while not EndTaskFlag:
    files = sorted(os.listdir(appSettings.ListenerTargetFolder), key=lambda filename: os.path.getmtime(appSettings.ListenerTargetFolder + "/" + filename), reverse=False)
    files.remove("README.md")

    if len(files) > 0:
        counter.reset()
        print("File detected: " + files[0])
        processExperiment(files[0])
    else:
        time.sleep(1)
        counter.increment()
