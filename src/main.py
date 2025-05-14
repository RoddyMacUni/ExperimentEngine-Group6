from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, GenericResponse, ResultSet
from AppSettings import AppSettings, GetAppSettings
import os
import time
from processing.Counter import Counter

EndTaskFlag: bool = False

appSettings: AppSettings = GetAppSettings()

def processExperiment(fileName: str, experimentId: str):
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
print("Listening for file on " + appSettings.ListenerTargetFolder)
counter = Counter(60, lambda minutes: print("No new file detected for " + str(minutes) + " minutes."))
while not EndTaskFlag:
    files = sorted(os.listdir(appSettings.ListenerTargetFolder), key=lambda filename: os.path.getmtime(appSettings.ListenerTargetFolder + "/" + filename), reverse=False)
    files.remove("README.md")

    if len(files) > 0:
        counter.reset()
        print("File detected: " + files[0])

        processExperiment(files[0], files[0].partition('.')[0]) #Remove file extension

        os.remove(appSettings.ListenerTargetFolder + "/" + files[0])
    else:
        time.sleep(1)
        counter.increment()
