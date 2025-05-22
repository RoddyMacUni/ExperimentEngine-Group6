from model.ResultSet import ResultSet
import json

def getMockExperiment() -> str:
    return '''{
    "networkConditions": {
        "delay": "50ms",
        "packetLoss": "2%"
    },
    "createdAt": "2024-04-01T10:00:00Z",
    "metricsRequested": [
        "PSNR",
        "PSNR"
    ],
    "encodingParameters": {
        "codec": "h264",
        "bitrate": "5000kbps",
        "resolution": "1920x1080"
    },
    "description": "An experiment testing video encodings.",
    "videoSources": [
        "video1.mp4",
        "video1.mp4"
    ],
    "id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    "experimentName": "My Test Experiment",
    "status": "pending"
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
    "Target": 109701,
    "Partner": "UWS",
    "Set": [
        {
            "Sequence": {
                "ECT": "Scalable",
                "COD": "SHVC",
                "ECM": "RANDOM ACCESS",
                "SPT": "1920X1080",
                "TMP": "30fps",
                "QUA": 27,
                "DPT": 8,
                "GAM": 0,
                "DURATION": "5",
                "VID": "Beauty"
            },
            "Network": "001003",
            "Results": [
                {
                    "Subject": "UWS1009",
                    "Bitrate": 100,
                    "PSNR": 100,
                    "SSIM": 100,
                    "VMAP": 100
                },
                {
                    "Subject": "UWS1034",
                    "Bitrate": 100,
                    "PSNR": 100,
                    "SSIM": 100,
                    "VMAP": 100
                },
                {
                    "Subject": "UWS1069",
                    "Bitrate": 100,
                    "PSNR": 100,
                    "SSIM": 100,
                    "VMAP": 100
                },
                {
                    "Subject": "UWS1083",
                    "Bitrate": 100,
                    "PSNR": 100,
                    "SSIM": 100,
                    "VMAP": 100
                }
            ]
        }
    ]
}'''

def getMockResultObject() -> ResultSet:
    return ResultSet(json.loads(getMockResultString()))