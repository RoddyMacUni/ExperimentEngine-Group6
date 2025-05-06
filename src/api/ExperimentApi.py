from src.api.BaseApi import BaseApi
from src.model.Experiment import Experiment
import requests

class ExperimentApi(BaseApi):
    def getExperimentById(self, id: str) -> Experiment:
        return requests.get(self.baseUrl + "/experiments/" + id)
    
