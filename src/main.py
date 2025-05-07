from api.ExperimentApi import ExperimentApi, Experiment

#Listen for new file

#Get data
experiment: Experiment = ExperimentApi("http://localhost:5001").getExperimentById("CHANGE THIS")

#Run through network

#Get metrics

#Send result

print(experiment.id)