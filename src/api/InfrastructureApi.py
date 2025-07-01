from api.BaseAuthenticatedApi import BaseAuthenticatedApi
from model.Network import Network
from api.TokenManager import TokenManager
from dacite import from_dict
import requests

class InfrastructureApi(BaseAuthenticatedApi):
    def getNetworkProfileById(self, id: str) -> Network:
        response = requests.get(self.baseUrl + "/Network/" + id, headers=self.tokenManager.getTokenAsAuthHeader())
        response.raise_for_status()
        return from_dict(data_class=Network, data=response.json())