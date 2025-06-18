from api.BaseApi import BaseApi
from model.Network import Network
from dacite import from_dict
import requests

class InfrastructureApi(BaseApi):
    def getNetworkProfileById(self, id: str) -> Network:
        response = requests.get(self.baseUrl + "/Network/" + id)
        response.raise_for_status()
        return from_dict(data_class=Network, data=response.json())