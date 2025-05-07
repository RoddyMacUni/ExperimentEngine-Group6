from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, GenericResponse, ResultSet
from AppSettings import AppSettings, GetAppSettings
import json

appSettings: AppSettings = GetAppSettings()

#Listen for new file

#Get data
experiment: Experiment = ExperimentApi(appSettings.ExperimentsEndpoint).getExperimentById("TODO")

#Run through network

#Get metrics

#Send result
resultResponse: GenericResponse = ResultApi(appSettings.ResultsEndpoint).sendResults("TODO", ResultSet("Test"))

print("Everything ran!")
print("ExperimentId: " + experiment.id)
print("ResultResponseMessage: " + resultResponse.message)