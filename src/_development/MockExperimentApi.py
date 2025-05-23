from flask import Flask
from StaticMockData import getMockExperiment

print("Starting API")
app = Flask(__name__)
app.debug = True


@app.route('/')
def test():
    return 'Hello World!'


@app.route('/experiments/<id>', methods = ['GET'])
def getExperimentById(id):
    return getMockExperiment()

app.run(port=5001)