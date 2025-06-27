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
    "TargetExperimentId": 109701,
    "Partner": "UWS",
    "OwnerId": 1235,
    "Set": [
        {
            "EncodingParameters": {
                "Video": "Beauty",
                "Duration": "5s",
                "Frames_to_Encode": 100,
                "FPS": 30,
                "ResWidth": 1920,
                "ResHeight": 1080,
                "OutputFile": "ID_1_encoded.yuv",
                "Encoder": "H264",
                "EncoderType": "Standard",
                "Bitrate": 45020,
                "YuvFormat": "4:0:0",
                "EncoderMode": "RANDOM ACCESS",
                "Quality": 27,
                "Depth": 12,
                "Gamut": "A",
                "QPISlice": 24,
                "QPPSlice": 24,
                "QPBSlice": 24,
                "IntraPeriod": 1,
                "BFrames": 2
            },
            "SequenceID": 1,
            "Network": "001003",
            "DistruptionProfile": 1,
            "Results": {
                "Bitrate": 100,
                "PSNR": 100,
                "SSIM": 100,
                "VMAF": 100
            }
        },
        {
            "EncodingParameters": {
                "Video": "Beauty",
                "Duration": "5s",
                "Frames_to_Encode": 100,
                "FPS": 30,
                "ResWidth": 1920,
                "ResHeight": 1080,
                "OutputFile": "ID_1_encoded.yuv",
                "Encoder": "H264",
                "EncoderType": "Standard",
                "Bitrate": 45020,
                "YuvFormat": "4:0:0",
                "EncoderMode": "RANDOM ACCESS",
                "Quality": 27,
                "Depth": 12,
                "Gamut": "A",
                "QPISlice": 24,
                "QPPSlice": 24,
                "QPBSlice": 24,
                "IntraPeriod": 1,
                "BFrames": 2
            },
            "SequenceID": 1,
            "Network": "001003",
            "DistruptionProfile": 1,
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
