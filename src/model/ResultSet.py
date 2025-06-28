from dataclasses import dataclass
from typing import List

@dataclass
class VideoResultMetrics:
    Bitrate: float
    PSNR: float
    SSIM: float
    VMAF: float

@dataclass
class ResultSetItem():
    SequenceID: int
    NetworkTopologyId: int | None #TODO remove this, this is a bug on the backend!
    DistruptionProfileId: int
    EncodingParameters: dict
    Results: VideoResultMetrics

@dataclass
class ResultSet:
    Error: str | None
    TargetExperimentId: int
    OwnerId: int
    Sequences: List[ResultSetItem]