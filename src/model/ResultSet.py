from dataclasses import dataclass
from typing import List

@dataclass 
class Sequence:
    ECT: str
    COD: str
    ECM: str
    SPT: str
    TMP: str
    QUA: int
    DPT: int
    GAM: int
    DURATION: int
    VID: str

@dataclass
class VideoResultMetrics:
    Subject: str
    Bitrate: int
    PSNR: int
    SSIM: int
    VMAP: int

@dataclass
class ResultSetItem:
    Sequence: Sequence
    Network: str
    Results: List[VideoResultMetrics]

@dataclass
class ResultSet:
    Error: str | None
    Target: int
    Partner: str
    Set: List[ResultSetItem]