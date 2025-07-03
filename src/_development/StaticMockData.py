from dacite import from_dict
from model.ResultSet import ResultSet
import json

def getMockExperiment() -> str:
    return '''
    {
  "ExperimentName": "EE-G6-testing",
  "Description": "string",
  "status": "PENDING",
  "Sequences": [
    {
      "NetworkTopologyId": {
        "networkName": "Network Profile 1",
        "description": "Description of Network Profile 1",
        "packetLoss": 10,
        "delay": 1,
        "jitter": 1,
        "bandwidth": 32,
        "network_profile_id": 1
      },
      "NetworkDisruptionProfileId": 0,
      "EncodingParameters": {
        "additionalProp1": {}
      },
      "SequenceId": 15,
      "NetworkDisruptionProfile": null
    }
  ],
  "Id": 7,
  "CreatedAt": "2025-07-03T08:54:18.483473",
  "OwnerId": 17
}
    '''

def getMockOKResultResponse() -> str:
    return '''{
  "message": "OK"
}'''

def getMockErrorResultResponse() -> str:
    return '''{
  "code": "500",
  "message": "ERROR"
}'''

def getMockResultString() -> str:
    return '''{
    "Error": null,
    "TargetExperimentId": 1,
	"OwnerId": 1,
    "Sequences": [
        {
            "EncodingParameters": {
                "additionalProp1": "test"
            },
            "SequenceID": 1,
            "NetworkTopologyId": 999,
            "DistruptionProfileId": 1,
            "Results": {
                "Bitrate": 100,
                "PSNR": 100,
                "SSIM": 100,
                "VMAF": 100
            }
        }
    ]
}'''

def getMockResultObject() -> ResultSet:
    return from_dict(data_class=ResultSet, data=json.loads(getMockResultString()))


def getMockNetwork() -> str:
    return '''{
        "name": "Profile Network Name",
        "id": 999,
        "packetLoss": 5,
        "delay": 20,
        "jitter": 3,
        "bandwidth": 100
    }'''
