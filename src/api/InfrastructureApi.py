from api.BaseAuthenticatedApi import BaseAuthenticatedApi
from model.Network import Network
from api.TokenManager import TokenManager
from dacite import from_dict
import requests

class InfrastructureApi(BaseAuthenticatedApi):
    def getNetworkProfileById(self, id: str) -> Network:
        return Network("Faked Network", 0, 10, 1, 1, 32)