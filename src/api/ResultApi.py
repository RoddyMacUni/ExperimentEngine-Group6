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
    