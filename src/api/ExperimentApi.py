from api.BaseAuthenticatedApi import BaseAuthenticatedApi
from model.Experiment import Experiment
from api.TokenManager import TokenManager
from dacite import from_dict
import requests
import json

class ExperimentApi(BaseAuthenticatedApi):
    def getExperimentById(self, id: str) -> Experiment:
        response = requests.get(self.baseUrl + "/experiments/" + id, headers=self.tokenManager.getTokenAsAuthHeader())
        response.raise_for_status()
        return from_dict(data_class=Experiment, data=json.loads(response.text))
    
