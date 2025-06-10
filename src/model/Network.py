from dataclasses import dataclass

@dataclass
class Network:
    name: str
    id: int
    packetLoss: int
    delay: int
    jitter: int
    bandwidth: int