from dataclasses import dataclass
import json

@dataclass
class AppSettings:
    ExperimentsEndpoint: str
    ResultsEndpoint: str
    ListenerTargetFolder: str

def GetAppSettings():
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))          #TODO: Better way?
    dictionary = json.load(open(dir_path + "\\appsettings.json"))
    return AppSettings(**dictionary)