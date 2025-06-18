from dacite import from_dict
from model.ResultSet import ResultSet
import json

def getMockExperiment() -> str:
    return '''{
    "id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    "OwnerId": 1235,
    "createdAt": "2024-04-01T10:00:00Z",
    "description": "An experiment testing video encodings.",
    "experimentName": "My Test Experiment",
    "status": "pending",
    "Set": [
    {
        "SequenceId": 1,
        "NetworkTopologyId": "001",
        "networkDisruptionProfileId": 100,
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
        }
    }
    ]
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
