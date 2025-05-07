from dataclasses import dataclass

@dataclass
class NetworkConditions:
    delay: str
    packetLoss: str

@dataclass
class EncodingParameters:
    codec: str
    bitrate: str
    resolution: str

@dataclass
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