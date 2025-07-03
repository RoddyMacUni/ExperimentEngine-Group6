from api.BaseApi import BaseApi
from api.TokenManager import TokenManager

class BaseAuthenticatedApi(BaseApi):
    tokenManager: TokenManager
    
    def __init__(self, baseUrl: str, tokenManager: TokenManager):
        super().__init__(baseUrl)
        self.tokenManager = tokenManager