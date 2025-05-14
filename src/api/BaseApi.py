class BaseApi():
    baseUrl: str
    
    def __init__(self, baseUrl: str):
        self.baseUrl = baseUrl