from api.BaseAuthenticatedApi import BaseAuthenticatedApi
from api.TokenManager import TokenManager
from model.GenericResponse import GenericResponse
from model.ResultSet import ResultSet
from dataclasses import asdict

import requests

class ResultApi(BaseAuthenticatedApi):
    def sendResults(self, experimentId: str, results: ResultSet) -> GenericResponse:
        response = requests.post(url=(self.baseUrl + "/experiments/" + experimentId + "/results"), json=asdict(results), headers=self.tokenManager.getTokenAsAuthHeader())
        response.raise_for_status()
        return GenericResponse(**response.json())
    
    def sendError(self, experimentId: str, errorMessage: str, ownerId: int = -1, partner: str = "") -> GenericResponse:
        failedResultsJson = ResultSet(errorMessage, experimentId, ownerId, [])
        response = requests.post(url=(self.baseUrl + "/experiments/" + experimentId + "/results"), json=asdict(failedResultsJson), headers=self.tokenManager.getTokenAsAuthHeader())
        response.raise_for_status()
        return GenericResponse(**response.json())
    