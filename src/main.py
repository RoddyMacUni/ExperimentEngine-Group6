from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, GenericResponse, ResultSet

#Listen for new file

#Get data
experiment: Experiment = ExperimentApi("http://localhost:5001").getExperimentById("TODO")

#Run through network

#Get metrics

#Send result
resultResponse: GenericResponse = ResultApi("http://localhost:5002").sendResults("TODO", ResultSet("Test"))

print("Everything ran!")
print("ExperimentId: " + experiment.id)
print("ResultResponseMessage: " + resultResponse.message)