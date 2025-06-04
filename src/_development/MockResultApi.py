from flask import Flask, request
from StaticMockData import getMockOKResultResponse, getMockErrorResultResponse
from model.ResultSet import ResultSet
from dacite import from_dict
import json

print("Starting API")
app = Flask(__name__)
app.debug = True


@app.route('/')
def test():
    return 'Hello World!'


@app.route('/experiments/<experimentId>/results', methods = ['POST'])
def createResults(experimentId):
    try:
        resultSet: ResultSet = from_dict(data_class=ResultSet, data=json.loads(request.get_json(force=True)))
        return getMockOKResultResponse()
    except:
        return getMockErrorResultResponse()

app.run(port=5002)