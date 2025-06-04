from dataclasses import dataclass

@dataclass 
class EncodingParameters:
    Video: str
    Duration: str
    Frames_to_Encode: int
    FPS: int
    ResWidth: int
    ResHeight: int
    OutputFile: str
    Encoder: str
    EncoderType: str
    Bitrate: int
    YuvFormat: str
    EncoderMode: str
    Quality: int
    Depth: int
    Gamut: str
    QPISlice: int
    QPPSlice: int
    QPBSlice: int
    IntraPeriod: int
    BFrames: int


@dataclass
class ExperimentSetItem:
    SequenceId: int
    NetworkTopologyId: str
    networkDisruptionProfileId: int
    EncodingParameters: EncodingParameters

@dataclass
class Experiment:
    id: str
    OwnerId: int
    experimentName: str
    createdAt: str
    description: str
    status: str
    Set: list[ExperimentSetItem]