import subprocess
from subprocess import CompletedProcess, CalledProcessError
from os.path import isdir
from dataclasses import dataclass
from pathlib import Path

APP_DATA_PATH = "../experiment_data/"
TIMEOUT = 10                            # The longest an experiment can run for before being terminated (measured in seconds)

@dataclass
class NetworkConditions:
    id: int             # The id of this run of the experiment (changes for each run of the experiment)
    packet_loss: float   # The decimal fraction of the packets that should be discarded
    delay: int          # In milliseconds

    def __init__(self, id: int, delay: int, packet_loss: float):
        self.delay = delay
        self.packet_loss = packet_loss
        self.id = id

    """
    Runs a set experiment
    
    Parameters:
    None
    
    Returns:
    :return The path to the results file
    """
    def run(self):
        # Validate the experiment has not been run already
        if isdir(f"./{self.id}"):
            print("Experiment has already been run")
            exit(0)
            # TODO: identify how duplicate experiment runs can occur and decide whether we will support it or not

        # Create a new process and run the specified command, if the process takes more than the TIMEOUT value it will time out
        try:
            completed_experiment = subprocess.run(["bash", "./test-script.sh", str(self.id), f"{self.delay}ms", f"{self.packet_loss * 100}%"], timeout=TIMEOUT,
                                                  capture_output=True)
        except subprocess.TimeoutExpired:
            print("Experiment Timed out")
            exit(0)
            # TODO: Implement timout and define how the results should be presented to the ResultsDB

        # Validate the experiment has actually passed and handle any failures that may occur
        try:
            completed_experiment.check_returncode()
            if completed_experiment.stderr != b'':
                raise ValueError
        except (ValueError, CalledProcessError) as e:
            print("Experiment failed")
            handleFailedExperiment(completed_experiment)

# TODO: Implement error handling and define how the results should be presented to the ResultsDB
def handleFailedExperiment(completed_experiment: CompletedProcess):
    print(f"Experiment failed: {completed_experiment}")


if __name__ == "__main__":
    NetworkConditions(1, 1, 0.2).run()