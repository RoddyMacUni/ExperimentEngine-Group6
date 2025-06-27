from AppSettings import AppSettings, GetAppSettings
from api.BaseApi import BaseApi
from dataclasses import dataclass
from dacite import from_dict
import requests
import json

@dataclass
class tokenResponse:
    token: str

class TokenManager(BaseApi):
    appSettings: AppSettings
    token: str

    def fetchNewToken(self):
        response = requests.get(self.baseUrl + "/auth/login")
        response.raise_for_status()
        return from_dict(data_class=tokenResponse, data=json.loads(response.text))

    def getToken(self):
        if(self.token is None):
            return self.fetchNewToken()
        return self.token
        
    