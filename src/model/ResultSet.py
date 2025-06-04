from dataclasses import dataclass
from typing import List

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
class VideoResultMetrics:
    Bitrate: int
    PSNR: int
    SSIM: int
    VMAF: int

@dataclass
class ResultSetItem:
    EncodingParameters: EncodingParameters
    SequenceID: int
    Network: str
    DistruptionProfile: int 
    Results: VideoResultMetrics

@dataclass
class ResultSet:
    Error: str | None
    Partner: str
    TargetExperimentId: int
    OwnerId: int
    Set: List[ResultSetItem]