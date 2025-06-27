from dacite import from_dict
from model.ResultSet import ResultSet
import json

def getMockExperiment() -> str:
    return '''{
    "ExperimentName": "SampleExperiment 1",
    "Description": "Sample experiment for demo purposes",
    "status": "PENDING",
    "Sequences": [
        {
            "NetworkTopologyId": null,
            "NetworkDisruptionProfileId": 1,
            "EncodingParameters": {
                "additionalProp1": "test"
            },
            "SequenceId": 2,
            "NetworkDisruptionProfile": null
        }
    ],
    "Id": 1,
    "CreatedAt": "2025-06-27T13:50:42.305689",
    "OwnerId": 1
}'''

def getMockOKResultResponse() -> str:
    return '''{
  "code": "200",
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
            "NetworkTopologyId": 1,
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
        "id": 1,
        "packetLoss": 5,
        "delay": 20,
        "jitter": 3,
        "bandwidth": 100
    }'''
