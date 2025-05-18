from dataclasses import dataclass
import json

@dataclass
class AppSettings:
    ExperimentsEndpoint: str
    ResultsEndpoint: str
    ListenerTargetFolder: str

def GetAppSettings():
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dictionary = json.load(open(os.path.abspath(os.path.dirname(__file__)) + "/appsettings.json"))
    return AppSettings(**dictionary)