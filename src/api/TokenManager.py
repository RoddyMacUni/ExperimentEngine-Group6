from api.BaseApi import BaseApi
from AppSettings import AppSettings, GetAppSettings
from dataclasses import dataclass
from dacite import from_dict
import requests
import json
import datetime

@dataclass
class tokenResponse:
    token: str

class TokenManager(BaseApi):
    token: str | None
    lastFetched: str | None
    refreshSeconds: int

    def __init__(self, baseUrl, refreshSeconds: int = 300):
        super().__init__(baseUrl)
        self.token = None
        self.lastFetched = None
        self.refreshSeconds = refreshSeconds

    def fetchNewToken(self):
        appsettings: AppSettings = GetAppSettings()
        response = requests.post(self.baseUrl + "/auth/login", json={'username': appsettings.Username,'password': appsettings.Password})
        response.raise_for_status()
        responseObject: tokenResponse = from_dict(data_class=tokenResponse, data=json.loads(response.text))
        self.lastFetched = datetime.datetime.now()
        return responseObject.token
    
    def tokenNeedsRefreshed(self) -> bool:
        if(self.lastFetched is None):
            return True
        if(datetime.datetime.now() > self.lastFetched + datetime.timedelta(0, self.refreshSeconds)):
            return True
        return False

    def getToken(self):
        if(self.token is None or self.tokenNeedsRefreshed()):
            self.token = self.fetchNewToken()
        return self.token
    
    def getTokenAsAuthHeader(self):
        return {'Authorization': 'Bearer ' + self.getToken()}