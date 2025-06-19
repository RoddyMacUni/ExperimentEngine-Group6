import subprocess
from subprocess import CompletedProcess, CalledProcessError
from os.path import isdir
from dataclasses import dataclass

from api.InfrastructureApi import InfrastructureApi
from model import Network
from model.Experiment import ExperimentSetItem, Experiment

from exceptions.KnownProcessingException import KnownProcessingException
from video_processing.VMAF import VMAFEvaluator

APP_DATA_PATH = "../experiment_data/"

@dataclass
class NetworkEmulator:
    parent_experiment: Experiment   # Exists only to get the parent experiment's id to raise an exception if something goes wrong
    network_conditions: Network     # The disruption profile required for this experiment item
    network_type: str               # The network topology to test on - TODO: Only one network topology supported at this time
    command_timeout = 10            # The longest an experiment can run for before being terminated (measured in seconds)

    def __init__(self, experiment_item: ExperimentSetItem, parent_experiment: Experiment):
        self.network_conditions = InfrastructureApi.getNetworkProfileById(experiment_item.networkDisruptionProfileId)

        # TODO: Get network topology details from the Infra API when supported
        self.network_type = experiment_item.NetworkTopologyId

        # FIXME: Sort out metric collection
        # self.evaluator = VMAFEvaluator()

        self.command = self.build_experiment_command()

    """
    Builds the command needed to actually run the experiment on the required network
    """
    def build_experiment_command(self) -> str:
        # Get the command required to gather metrics
        # TODO: Actually get the command required to gather the metrics
        metric_command = "unimpl"

        # TODO: Clarify network types supported
        match self.network_type:
            case "001":
                driver_command = f"./virtual-network.sh {self.network_conditions.delay}ms {self.network_conditions.packetLoss}%"
            case _:
                # Throw exception if anything but a virtual network is required
                raise KnownProcessingException(f"network type {self.network_type} is not supported", self.parent_experiment.id)

        return f"{driver_command} {metric_command}"

    """
    Actually runs the command to execute the experiment and handles any failures that may occur
    """
    def run(self):

        # Create a new process and run the driver command, if the process takes more than the TIMEOUT value it will time out
        try:
            completed_experiment = subprocess.run(["bash", self.command], timeout=self.command_timeout, capture_output=True)
        except subprocess.TimeoutExpired:
            raise KnownProcessingException("Video streaming took too long", self.parent_experiment.id)

        # Validate the experiment has actually passed and handle any failures that may occur
        try:
            completed_experiment.check_returncode()
            if completed_experiment.stderr != b'':
                raise ValueError
        except (ValueError, CalledProcessError) as e:
             raise KnownProcessingException(f"Experiment failed: {completed_experiment} with error: {completed_experiment.stderr}", self.parent_experiment.id)
