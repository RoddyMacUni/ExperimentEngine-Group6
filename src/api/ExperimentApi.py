from api.BaseApi import BaseApi
from model.Experiment import Experiment
import requests

class ExperimentApi(BaseApi):
    def getExperimentById(self, id: str) -> Experiment:
        response = requests.get(self.baseUrl + "/experiments/" + id)
        response.raise_for_status()
        return Experiment(**response.json())
    
