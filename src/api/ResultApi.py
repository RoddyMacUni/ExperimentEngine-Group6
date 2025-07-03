import random

from api.BaseAuthenticatedApi import BaseAuthenticatedApi
from api.TokenManager import TokenManager
from model.GenericResponse import GenericResponse
from model.ResultSet import ResultSet
from dataclasses import asdict

import requests, json, os

class ResultApi(BaseAuthenticatedApi):
    def sendResults(self, experimentId: str, results: ResultSet) -> GenericResponse:
        try:
            variable = "temp" + str(random.randint(1,1000)) + ".json"
            file = open(variable, 'w+')
            json.dump(asdict(results), file)
            file.close()
            file2 = open(variable, 'r')
            response = requests.post(url=(self.baseUrl + "/experiments/" + experimentId + "/results"), headers=self.tokenManager.getTokenAsAuthHeader(), files={"file": file2})

            # Mark the experiment as complete
            _ = requests.put(url=(self.baseUrl + "/experiments/" + experimentId), headers=self.tokenManager.getTokenAsAuthHeader(), data='{"Status": "COMPLETE"}')
        except Exception as e:
            raise e
        finally:
            file2.close()
            #os.remove(file.name)

        response.raise_for_status()
        return GenericResponse(**response.json())


    
    def sendError(self, experimentId: str, errorMessage: str, ownerId: int = -1, partner: str = "") -> GenericResponse:
        failedResultsJson = ResultSet(errorMessage, experimentId, ownerId, [])

        try:
            file = open("temp.json", 'w+')
            json.dump(asdict(failedResultsJson), file)
            response = requests.post(url=(self.baseUrl + "/experiments/" + experimentId + "/results"), files={"file": file}, headers=self.tokenManager.getTokenAsAuthHeader())
        except Exception as e:
            raise e
        finally:
            file.close()
            os.remove(file.name)
        
        response.raise_for_status()
        return GenericResponse(**response.json())
    