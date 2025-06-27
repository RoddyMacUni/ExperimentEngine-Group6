from model.Experiment import Experiment, SequenceItem
from model.ResultSet import ResultSet, ResultSetItem, VideoResultMetrics
from processing.ResultCompiler import ResultCompiler

import os

def getEmptyEncodingParameters() -> any:
    return { "parameter": "value" }

def getSimpleResultSetItem(sequenceNum: int) -> ResultSetItem:
    return ResultSetItem(getEmptyEncodingParameters(), sequenceNum, '0', 0, VideoResultMetrics(0, 0, 0, 0))

def getSimpleResultSet() -> ResultSet:
    return ResultSet(None, "", 0, 0, [ getSimpleResultSetItem(0) ])

def getSimpleSequenceItem(sequenceNum: int) -> SequenceItem:
    return SequenceItem(sequenceNum, 0, 0, getEmptyEncodingParameters())

def getSimpleExperiment() -> Experiment:
    return Experiment("0", 0, "test experiment", "now", "description", "in progress", [ getSimpleSequenceItem(0) ])


def test_will_accept_full_result_file():
    experiment: Experiment = getSimpleExperiment()
    assert not os.path.exists(ResultCompiler().getFileName(experiment))

    result = ResultCompiler().CompileResultsFile(getSimpleResultSet(), getSimpleExperiment())

    assert result is not None
    assert result.TargetExperimentId == int(experiment.Id)

    assert not os.path.exists(ResultCompiler().getFileName(experiment))

def test_will_save_partial_result_file():
    experiment: Experiment = getSimpleExperiment()
    experiment.Set.append(getSimpleSequenceItem(1))
    assert not os.path.exists(ResultCompiler().getFileName(experiment))

    result = ResultCompiler().CompileResultsFile(getSimpleResultSet(), experiment)

    assert result is None

    assert os.path.exists(ResultCompiler().getFileName(experiment))
    os.remove(ResultCompiler().getFileName(experiment))
    assert not os.path.exists(ResultCompiler().getFileName(experiment))

def test_will_combine_partial_result_files():
    experiment: Experiment = getSimpleExperiment()
    experiment.Set.append(getSimpleSequenceItem(1))
    assert not os.path.exists(ResultCompiler().getFileName(experiment))

    resultCompiler = ResultCompiler()
    result = resultCompiler.CompileResultsFile(getSimpleResultSet(), experiment)

    assert result is None

    assert os.path.exists(ResultCompiler().getFileName(experiment))

    result = resultCompiler.CompileResultsFile(getSimpleResultSet(), experiment)

    assert result is not None
    assert result.TargetExperimentId == int(experiment.Id)

    assert not os.path.exists(ResultCompiler().getFileName(experiment))