from model.Experiment import Experiment, ExperimentSetItem, EncodingParameters
from model.Network import Network
from network_emulation.NetworkEmulation import NetworkEmulator
import unittest

# This isn't used but is required for testing purposes
mock_encoder_params: EncodingParameters = EncodingParameters(
	Video= "Beauty",
    Duration= "5s",
    Frames_to_Encode= 100,
    FPS= 30,
    ResWidth= 1920,
    ResHeight= 1080,
    OutputFile= "ID_1_encoded.yuv",
    Encoder= "H264",
    EncoderType= "Standard",
    Bitrate= 45020,
    YuvFormat= "4:0:0",
    EncoderMode= "RANDOM ACCESS",
    Quality= 27,
    Depth= 12,
    Gamut= "A",
    QPISlice= 24,
    QPPSlice= 24,
    QPBSlice= 24,
    IntraPeriod= 1,
    BFrames= 2
)

class TestNetworkEmulation(unittest.TestCase):
	"""
	Ensures the command used to run the video streaming is correct on the golden path
	"""
	def test_virtual_network_driver_command(self):
		# Create test experiment from scratch
		test_exp_item :ExperimentSetItem = ExperimentSetItem(
			0,
			'001',
			100,
			EncodingParameters= mock_encoder_params,
		)

		test_exp: Experiment = Experiment(
			"1",
			1,
			"test_experiment",
			"",
			"",
			"",
			[test_exp_item]
		)

		network = Network(
			name="test_network",
			id=1,
			packetLoss=9,
			delay=11,
			jitter=11,
			bandwidth=100
		)

		net_emu: NetworkEmulator = NetworkEmulator(test_exp_item, test_exp, network)
		actual_cmd = net_emu.build_experiment_command()

		expected_cmd = './virtual-network.sh 0 11 9 /tmp/0.mp4 /tmp/0-distorted.mp4 '
		self.assertEqual(actual_cmd, expected_cmd)
