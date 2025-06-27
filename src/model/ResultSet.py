from dataclasses import dataclass
from typing import List

@dataclass
class VideoResultMetrics:
    Bitrate: int
    PSNR: int
    SSIM: int
    VMAF: int

@dataclass
class ResultSetItem:
    EncodingParameters: dict
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