from flask import Flask, request
from AppSettings import AppSettings, GetAppSettings
import os

print("Starting API")
app = Flask(__name__)

@app.route('/')
def test():
    return 'Hello World!'

# Uploads file to the configured directory
# Takes form data with 'file' (file) 'experimentId' (string) and 'sequenceNumber' (int)
# This enforces naming convention
@app.route('/encoded/upload', methods = ['POST'])
def getExperimentById():
    if 'file' not in request.files:
        return "File not found - make sure the form data has a 'file' field with the attached video", 400
    if 'experimentId' not in request.form or 'sequenceNumber' not in request.form:
        return "Experiment ID (string) and sequence number (integer) must be provided in the form data", 400
    
    #TODO: Validate mp4?, authenticate?
    file = request.files['file']
    filename = request.form['experimentId'] + "_" + request.form['sequenceNumber'] + "_encoded.mp4"

    filePath = os.path.join(GetAppSettings().ListenerTargetFolder, filename)
    file.save(filePath)

    return "Video received and saved successfully", 200

app.run(port=5000)