from dataclasses import dataclass
from typing import List
from model.Experiment import EncodingParameters

@dataclass
class VideoResultMetrics:
    Bitrate: float
    PSNR: float
    SSIM: float
    VMAF: float

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