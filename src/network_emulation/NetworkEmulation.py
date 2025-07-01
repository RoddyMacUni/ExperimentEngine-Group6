import subprocess
from pathlib import PurePath
from subprocess import CompletedProcess, CalledProcessError
from os.path import exists
from dataclasses import dataclass

from model import Network
from model.Experiment import SequenceItem, Experiment

from exceptions.KnownProcessingException import KnownProcessingException

APP_DATA_PATH = "../experiment_data/"

@dataclass
class NetworkEmulator:
    parent_experiment: Experiment   # Exists only to get the parent experiment's id to raise an exception if something goes wrong
    experiment_item: SequenceItem
    network_conditions: Network     # The disruption profile required for this experiment item
    network_type: int               # The network topology to test on - TODO: Only one network topology supported at this time
    source_file: str                # The file under test
    disrupted_file: str             # Path to the video that has been streamed through the network

    command_timeout = 120            # The longest an experiment can run for before being terminated (measured in seconds)

    def __init__(self, experiment_item: SequenceItem, parent_experiment: Experiment, network_conditions: Network, source_filename: str) -> None:
        self.network_conditions = network_conditions
        self.experiment_item = experiment_item
        self.parent_experiment = parent_experiment
        self.network_type = self.experiment_item.NetworkTopologyId  # TODO: Get network topology details from the Infra API when supported


        # Ensure the file still exists
        if not exists(source_filename):
            raise KnownProcessingException(f"source file f{source_filename} not found", str(self.parent_experiment.Id))

        # Set the source and destination paths
        self.source_file = source_filename
        self.disrupted_file = PurePath(PurePath(source_filename).parent, f"{parent_experiment.Id}-{experiment_item.SequenceId}-disrupted.mp4").__str__()

        # Generate the command required to run the experiment
        self.command = self.build_experiment_command()

    """
    Builds the command needed to actually run the experiment on the required network
    """
    def build_experiment_command(self) -> str:
        # TODO: Clarify network types supported
        match self.network_type:
            case 1:
                # TODO Rework command generation
                driver_command = (f"bash /root/ExperimentEngine-Group6/src/network_emulation/virtual-network.sh "
                                  f"{self.experiment_item.SequenceId} "
                                  f"{self.network_conditions.delay} "
                                  f"{self.network_conditions.packetLoss} "
                                  f"{self.source_file} "
                                  f"{self.disrupted_file}")
            case 999: # A demo mode
                driver_command = (f"bash /root/ExperimentEngine-Group6/src/network_emulation/demo-mode.sh"
                                  f" {PurePath(self.disrupted_file).parent}/sample_degraded.mp4 "
                                  f" {self.disrupted_file}")

            case _:
                # Throw exception if anything but a virtual network is required
                raise KnownProcessingException(f"network type {self.network_type} is not supported", str(self.parent_experiment.Id))

        return f"{driver_command}"

    """
    Actually runs the command to execute the experiment and handles any failures that may occur.
    Returns the disrupted video and the output of the network_emulation script
    """
    def run(self) -> tuple:

        # Create a new process and run the driver command, if the process takes more than the TIMEOUT value it will time out
        try:
            completed_experiment: CompletedProcess = subprocess.run([self.command], timeout=self.command_timeout, capture_output=True, shell=True)
        except subprocess.TimeoutExpired:
            raise KnownProcessingException("Video streaming took too long", str(self.parent_experiment.Id))

        # Validate the experiment has actually passed and handle any failures that may occur
        try:
            completed_experiment.check_returncode()
        except CalledProcessError:
             raise KnownProcessingException(f"Experiment failed: {completed_experiment} with error: {completed_experiment.stderr}", str(self.parent_experiment.Id))

        return self.disrupted_file, f"{completed_experiment.stdout.decode('utf-8')}\n[FFMPEG_LOG]\n{completed_experiment.stderr.decode('utf-8')}"