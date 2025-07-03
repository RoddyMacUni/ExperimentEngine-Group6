from dataclasses import dataclass

@dataclass
class SequenceItem:
    SequenceId: int
    NetworkTopologyId: int | None #TODO remove this, this is a bug on the backend!!
    NetworkDisruptionProfileId: int
    EncodingParameters: dict

@dataclass
class Experiment:
    Id: int
    OwnerId: int
    ExperimentName: str
    CreatedAt: str
    Description: str
    status: str
    Sequences: list[SequenceItem]