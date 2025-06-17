from model.ResultSet import ResultSet, ResultSetItem

#Attempts to compile full result from partial one
#Requires partialResults to contain all top-level data
#Returns none if could not compile full result
def CompileResultsFile(partialResults: ResultSet) -> ResultSet | None:
    