from api.BaseApi import BaseApi
from model.Experiment import Experiment
from dacite import from_dict
import requests
import json

class ExperimentApi(BaseApi):
    def getExperimentById(self, id: str) -> Experiment:
        response = requests.get(self.baseUrl + "/experiments/" + id)
        response.raise_for_status()
        return from_dict(data_class=Experiment, data=json.loads(response.text))
    
