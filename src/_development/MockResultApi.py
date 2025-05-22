from flask import Flask
from StaticMockData import getMockOKResultResponse, getMockErrorResultResponse
from model.ResultSet import ResultSet, ResultSetItem, Sequence, VideoResultMetrics

print("Starting API")
app = Flask(__name__)
app.debug = True


@app.route('/')
def test():
    return 'Hello World!'


@app.route('/experiments/<experimentId>/results', methods = ['POST'])
def createResults(experimentId):
    return getMockOKResultResponse()

app.run(port=5002)