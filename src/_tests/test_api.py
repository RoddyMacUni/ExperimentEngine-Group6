import sys
import os
import requests_mock
import json

#Add src to PATH
srcPath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(srcPath)
from api.ResultApi import ResultApi, ResultSet, GenericResponse
from api.ExperimentApi import ExperimentApi, Experiment
import _development.StaticMockData as mockData


def test_results_api():
    resultsApi = ResultApi('http://test.com')

    with requests_mock.Mocker() as m:
        m.post('http://test.com/experiments/12345/results', json=json.loads(mockData.getMockResultResponse()))       

        response: GenericResponse = resultsApi.sendResults("12345", ResultSet("test"))
        assert response.code == "200"
        assert response.message == "OK"

def test_experiments_api():
    experimentApi = ExperimentApi('http://test.com')

    with requests_mock.Mocker() as m:
        m.get('http://test.com/experiments/12345', json=json.loads(mockData.getMockExperiment()))       

        response: Experiment = experimentApi.getExperimentById("12345")
        assert response.id == "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
        assert response.description == "An experiment testing video encodings."
