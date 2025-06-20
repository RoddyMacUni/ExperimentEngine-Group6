from network_emulation.NetworkEmulation import NetworkEmulator
from _development.MockExperimentApi import getExperimentById

"""
Ensures the command used to run the video streaming is correct on the golden path
"""
def test_virtual_network_driver_command():
	# Get the test data from the static mock api
	experiment = getExperimentById(1)
	experiment_item = experiment.Set[1]
	net_emu: NetworkEmulator = NetworkEmulator(experiment_item, experiment, "../in/test.mp4","../in/test-distorted.mp4")
	actual_cmd = net_emu.build_experiment_command()
	expected_cmd = './virtual-network.sh 1 1ms 10% ../in/test.mp4 ../in/test-distorted.mp4'
	assert actual_cmd == expected_cmd