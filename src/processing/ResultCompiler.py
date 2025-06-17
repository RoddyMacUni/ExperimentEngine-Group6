from model.ResultSet import ResultSet, ResultSetItem
from model.Experiment import Experiment
from AppSettings import AppSettings, GetAppSettings

import os
import json
from dacite import from_dict

class ResultCompiler:
    partialResultsTargetFolder: str

    def __init__(self):
        self.partialResultsTargetFolder = GetAppSettings().PartialResulsTargetFolder

    def getFileName(self, experiment: Experiment) -> str:
        #Returns the file name for the partial results file
        return self.partialResultsTargetFolder + "/" + experiment.id

    #Attempts to compile full result from partial one
    #Requires partialResults to contain all top-level data
    #Returns none if could not compile full result
    def CompileResultsFile(self, partialResults: ResultSet, experiment: Experiment) -> ResultSet | None:
        #Check if existing results file exists for experiment, if one exists load and append data
        currentResults: ResultSet
        if os.path.exists(self.getFileName(experiment)):
            file = open(self.getFileName(experiment), 'r')

            currentResults: ResultSet = from_dict(data_class=ResultSet, data=json.loads(file.read()))
            file.close()

            currentResults.Set.extend(partialResults.Set)
        #Otherwise, use partial file
        else:
            currentResults = partialResults

        #Check if results has all sequence items, if not then save it and return None
        if len(currentResults.Set) == len(experiment.Set):
            file = open(self.getFileName(experiment), 'w')
            file.write(json.dumps(currentResults.to_dict(), indent=4))
            file.close()
            return None

        #Otherwise, return the full result file
        return currentResults