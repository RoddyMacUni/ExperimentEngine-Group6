from flask import Flask
from StaticMockData import getMockExperiment

print("Starting API")
app = Flask(__name__)
app.debug = True


@app.route('/')
def test():
    return 'Hello World!'


@app.route('/Network/<id>', methods = ['GET'])
def getNetworkProfileById(id):
    return getNetworkProfileById()

app.run(port=5001)