from flask import Flask

print("Starting API")
app = Flask(__name__)
app.debug = True


@app.route('/')
def test():
    return 'Hello World!'


@app.route('/experiments/<experimentId>/results', methods = ['POST'])
def createResults(experimentId):
    return '''{
  "code": "200",
  "message": "OK"
}'''

app.run(port=5002)