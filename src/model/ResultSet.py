from dataclasses import dataclass
from typing import List

@dataclass
class VideoResultMetrics:
    Bitrate: float
    PSNR: float
    SSIM: float
    VMAF: float

@dataclass
class ResultSetItem:
    SequenceID: int
    NetworkTopologyId: int
    DistruptionProfileId: int
    EncodingParameters: dict
    Results: VideoResultMetrics

@dataclass
class ResultSet:
    Error: str | None
    TargetExperimentId: int
    OwnerId: int
    Sequences: List[ResultSetItem]