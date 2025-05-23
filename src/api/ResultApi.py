from api.BaseApi import BaseApi
from model.GenericResponse import GenericResponse
from model.ResultSet import ResultSet

import requests

class ResultApi(BaseApi):
    def sendResults(self, experimentId: str, results: ResultSet) -> GenericResponse:
        response = requests.post(url=(self.baseUrl + "/experiments/" + experimentId + "/results"), json=results.__dict__)
        response.raise_for_status()
        return GenericResponse(**response.json())
    