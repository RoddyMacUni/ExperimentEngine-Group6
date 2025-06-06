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

#This mocker does not support request bodies
#So this is to cover testing the result body can be parsed
def test_results_parsing():
    object: ResultSet = mockData.getMockResultObject()
    assert object.Partner == 'UWS'
    assert object.Set[0].EncodingParameters.Video == "Beauty"
    assert object.Set[0].Results.Bitrate == 100

def test_results_api():
    resultsApi = ResultApi('http://test.com')

    with requests_mock.Mocker() as m:
        m.post('http://test.com/experiments/12345/results', json=json.loads(mockData.getMockOKResultResponse()))       

        response: GenericResponse = resultsApi.sendResults("12345", mockData.getMockResultObject())
        assert response.code == "200"
        assert response.message == "OK"

def test_experiments_api():
    experimentApi = ExperimentApi('http://test.com')

    with requests_mock.Mocker() as m:
        m.get('http://test.com/experiments/12345', json=json.loads(mockData.getMockExperiment()))       

        response: Experiment = experimentApi.getExperimentById("12345")
        assert response.id == "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
        assert response.description == "An experiment testing video encodings."
        assert response.Set[0].EncodingParameters.Video == "Beauty"
