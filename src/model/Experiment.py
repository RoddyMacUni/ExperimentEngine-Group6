class NetworkConditions:
    delay: str
    packetLoss: str

class EncodingParameters:
    codec: str
    bitrate: str
    resolution: str

class Experiment:
    networkConditions: NetworkConditions
    createdAt: str
    metricsRequested: list[str]
    encodingParameters: EncodingParameters
    description: str
    videoSources: list[str]
    id: str
    experimentName: str
    status: str