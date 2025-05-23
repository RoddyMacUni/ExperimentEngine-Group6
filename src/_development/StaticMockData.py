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

def getMockResultResponse() -> str:
    return '''{
  "code": "200",
  "message": "OK"
}'''