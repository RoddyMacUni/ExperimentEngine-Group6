from dataclasses import dataclass
from model.Network import Network

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
    
# The API is returning:
# {
#   "ExperimentName": "EE-G6-testing",
#   "Description": "string",
#   "status": "PENDING",
#   "Sequences": [
#     {
#       "NetworkTopologyId": {
#         "networkName": "Network Profile 1",
#         "description": "Description of Network Profile 1",
#         "packetLoss": 10,
#         "delay": 1,
#         "jitter": 1,
#         "bandwidth": 32,
#         "network_profile_id": 1
#       },
#       "NetworkDisruptionProfileId": 0,
#       "EncodingParameters": {
#         "additionalProp1": {}
#       },
#       "SequenceId": 15,
#       "NetworkDisruptionProfile": null
#     }
#   ],
#   "Id": 7,
#   "CreatedAt": "2025-07-03T08:54:18.483473",
#   "OwnerId": 17
# }
@dataclass 
class IncorrectDemoExperimentSequenceItem:
    SequenceId: int
    NetworkTopologyId: int
    NetworkDisruptionProfileId: int
    EncodingParameters: dict

@dataclass
class IncorrectDemoExperiment:
    Id: int
    OwnerId: int
    ExperimentName: str
    CreatedAt: str
    Description: str
    status: str
    Sequences: list[IncorrectDemoExperimentSequenceItem]

def IncorrectDemoToOurExperiment(b: IncorrectDemoExperiment) -> Experiment:
    sequenceItems: list[SequenceItem] = []

    for i in range(len(b.Sequences)):
        bs: IncorrectDemoExperimentSequenceItem = b.Sequences[i]
        sequenceItems.append(SequenceItem(bs.SequenceId, bs.NetworkTopologyId, bs.NetworkDisruptionProfileId, bs.EncodingParameters))

    return Experiment(b.Id, b.OwnerId, b.ExperimentName, b.CreatedAt, b.Description, b.status, sequenceItems)