from api.BaseApi import BaseApi
from model.GenericResponse import GenericResponse
from model.ResultSet import ResultSet
from dataclasses import asdict

import requests

class ResultApi(BaseApi):
    def sendResults(self, experimentId: str, results: ResultSet) -> GenericResponse:
        response = requests.post(url=(self.baseUrl + "/experiments/" + experimentId + "/results"), json=asdict(results))
        response.raise_for_status()
        return GenericResponse(**response.json())
    
    def sendError(self, experimentId: str, errorMessage: str, ownerId: int = -1, partner: str = "") -> GenericResponse:
        failedResultsJson = ResultSet(errorMessage, partner, experimentId, ownerId, [])
        response = requests.post(url=(self.baseUrl + "/experiments/" + experimentId + "/results"), json=asdict(failedResultsJson))
        response.raise_for_status()
        return GenericResponse(**response.json())
    