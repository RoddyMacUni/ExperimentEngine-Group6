from multiprocessing import Process
import subprocess
import sys
import os
from time import sleep

#Add src to PATH
srcPath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(srcPath)
from api.ExperimentApi import ExperimentApi, Experiment
from api.ResultApi import ResultApi, ResultSet, GenericResponse
from AppSettings import GetAppSettings, AppSettings

def test_results_api():
    resultsProcess = Process(target=subprocess.run, args=[["python", srcPath + "/_development/MockResultApi.py"]])
    
    resultsProcess.start()

    sleep(10)
    appSettings: AppSettings = GetAppSettings()
    resultsApi = ResultApi(appSettings.ResultsEndpoint)

    response: GenericResponse = resultsApi.sendResults("12345", ResultSet("test"))
    assert response.code == "200"
    assert response.message == "OK"

    resultsProcess.terminate()

def test_experiments_api():
    experimentsProcess = Process(target=subprocess.run, args=[["python", srcPath + "/_development/MockExperimentApi.py"]])
    
    experimentsProcess.start()

    sleep(10)
    appSettings: AppSettings = GetAppSettings()
    experimentsApi = ExperimentApi(appSettings.ExperimentsEndpoint)

    response: Experiment = experimentsApi.getExperimentById("12345")
    assert response.description == "An experiment testing video encodings."
    assert response.id == "046b6c7f-0b8a-43b9-b35d-6489e6daee91"

    experimentsProcess.terminate()
