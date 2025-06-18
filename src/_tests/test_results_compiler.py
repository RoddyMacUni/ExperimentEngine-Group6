from model.Experiment import Experiment, ExperimentSetItem
from model.ResultSet import ResultSet, ResultSetItem, EncodingParameters, VideoResultMetrics
from processing.ResultCompiler import ResultCompiler

import os

def getEmptyEncodingParameters() -> EncodingParameters:
    return EncodingParameters("", "", 0, 0, 0, 0, "", "", "", 0, "", "", 0, 0, "", 0, 0, 0, 0, 0)

def getSimpleResultSetItem(sequenceNum: int) -> ResultSetItem:
    return ResultSetItem(getEmptyEncodingParameters(), sequenceNum, '0', 0, VideoResultMetrics(0, 0, 0, 0))

def getSimpleResultSet() -> ResultSet:
    return ResultSet(None, "", 0, 0, [ getSimpleResultSetItem(0) ])

def getSimpleExperimentSetItem(sequenceNum: int) -> ExperimentSetItem:
    return ExperimentSetItem(sequenceNum, 0, 0, getEmptyEncodingParameters())

def getSimpleExperiment() -> Experiment:
    return Experiment("0", 0, "test experiment", "now", "description", "in progress", [ getSimpleExperimentSetItem(0) ])

def test_will_accept_full_result_file():
    experiment: Experiment = getSimpleExperiment()

    result = ResultCompiler().CompileResultsFile(getSimpleResultSet(), getSimpleExperiment())

    assert result is not None
    assert result.TargetExperimentId == int(experiment.id)

def test_will_save_partial_result_file():
    pass