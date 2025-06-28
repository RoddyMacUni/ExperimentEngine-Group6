from api.BaseApi import BaseApi
from AppSettings import AppSettings, GetAppSettings
from dataclasses import dataclass
from dacite import from_dict
import requests
import json

@dataclass
class tokenResponse:
    token: str

class TokenManager(BaseApi):
    token: str | None

    def __init__(self, baseUrl):
        super().__init__(baseUrl)
        self.token = None

    def fetchNewToken(self):
        appsettings: AppSettings = GetAppSettings()
        response = requests.post(self.baseUrl + "/auth/login", json={'username': appsettings.Username,'password': appsettings.Password})
        response.raise_for_status()
        responseObject: tokenResponse = from_dict(data_class=tokenResponse, data=json.loads(response.text))
        return responseObject.token

    def getToken(self):
        if(self.token is None):
            self.token = self.fetchNewToken()
        return self.token
    
    def getTokenAsAuthHeader(self):
        return {'Authorization': 'Bearer ' + self.getToken()}