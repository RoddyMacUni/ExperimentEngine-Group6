from model.ResultSet import ResultSet, ResultSetItem
from model.Experiment import Experiment
from AppSettings import AppSettings, GetAppSettings
from dataclasses import asdict
from exceptions.KnownProcessingException import KnownProcessingException
import os
import json
from dacite import from_dict

class ResultCompiler:
    srcFolder: str
    partialResultsTargetFolder: str

    def __init__(self):
        self.srcFolder = os.path.abspath(os.path.dirname(__file__)) + "/../"
        self.partialResultsTargetFolder = self.srcFolder + GetAppSettings().PartialResulsTargetFolder

    def getFileName(self, experiment: Experiment) -> str:
        #Returns the file name for the partial results file
        return self.partialResultsTargetFolder + "/" + experiment.id

    #Attempts to compile full result from partial one
    #Requires partialResults to contain all top-level data
    #Returns none if could not compile full result
    def CompileResultsFile(self, partialResults: ResultSet, experiment: Experiment) -> ResultSet | None:
        #If these do not match, it is a logical error in the program
        if not (partialResults.TargetExperimentId == experiment.id): raise Exception("Experiment Id's do not match")
        
        #Check if existing results file exists for experiment, if one exists load and append data
        currentResults: ResultSet
        if os.path.exists(self.getFileName(experiment)):
            file = open(self.getFileName(experiment), 'r')

            currentResults: ResultSet = from_dict(data_class=ResultSet, data=json.loads(file.read()))
            file.close()

            currentResults.Set.append(partialResults.Set)
        #Otherwise, use partial file
        else:
            currentResults = partialResults

        #Check if results has all sequence items
        if len(currentResults.Set) == len(experiment.Set):
            if os.path.exists(self.getFileName(experiment)):
                os.remove(self.getFileName(experiment))
            return currentResults
        
        #If not then save it and return None
        file = open(self.getFileName(experiment), 'w')
        file.write(json.dumps(asdict(currentResults), indent=4))
        file.close()
        return None
        