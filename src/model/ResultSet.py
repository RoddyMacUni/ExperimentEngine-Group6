from dataclasses import dataclass
from typing import List
from model.Experiment import EncodingParameters

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