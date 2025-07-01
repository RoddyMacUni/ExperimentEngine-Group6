import sys
import os
import requests_mock
from requests_mock import Mocker
import json

#Add src to PATH
srcPath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(srcPath)
from api.ResultApi import ResultApi, ResultSet, GenericResponse
from api.ExperimentApi import ExperimentApi, Experiment
from api.InfrastructureApi import InfrastructureApi, Network
from api.TokenManager import TokenManager
import _development.StaticMockData as mockData

tokenManager: TokenManager = TokenManager("http://localhost:2000/fake")

#This mocker does not support request bodies
#So this is to cover testing the result body can be parsed
def test_results_parsing():
    object: ResultSet = mockData.getMockResultObject()
    assert object.OwnerId == 1
    assert object.Sequences[0].SequenceID == 1

def test_results_api():
    resultsApi = ResultApi('http://localhost:2000/fake', tokenManager)

    with requests_mock.Mocker() as m:
        m.post('http://localhost:2000/fake/experiments/12345/results', json=json.loads(mockData.getMockOKResultResponse()))       
        m.post('http://localhost:2000/fake/auth/login', text='{"token": "abc"}')

        response: GenericResponse = resultsApi.sendResults("12345", mockData.getMockResultObject())
        assert response.message == "OK"

def test_experiments_api():
    experimentApi = ExperimentApi('http://localhost:2000/fake', tokenManager)

    with requests_mock.Mocker() as m:
        m.get('http://localhost:2000/fake/experiments/1', json=json.loads(mockData.getMockExperiment()))       
        m.post('http://localhost:2000/fake/auth/login', text='{"token": "abc"}')

        response: Experiment = experimentApi.getExperimentById("1")
        assert response.Id == 1
        assert response.Description == "Sample experiment for demo purposes"
        assert response.Sequences[0].EncodingParameters != None

def test_infrastructure_api():
    infraApi = InfrastructureApi('http://localhost:2000/fake', tokenManager)

    with requests_mock.Mocker() as m:
        m.get(
            'http://localhost:2000/fake/Network/1',
            json=json.loads(mockData.getMockNetwork())
        )
        m.post('http://localhost:2000/fake/auth/login', text='{"token": "abc"}')

        response: Network = infraApi.getNetworkProfileById("1")

        assert response.name == "Profile Network Name"
        assert response.id == 1
        assert response.packetLoss == 5
        assert response.delay == 20
        assert response.jitter == 3
        assert response.bandwidth == 100