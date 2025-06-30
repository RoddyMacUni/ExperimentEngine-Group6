from exceptions.KnownProcessingException import KnownProcessingException
from model.Experiment import Experiment, ExperimentSetItem, EncodingParameters
from model.Network import Network
from network_emulation.NetworkEmulation import NetworkEmulator
import unittest
from platform import freedesktop_os_release
from os.path import exists
from os import remove

class TestNetworkEmulation(unittest.TestCase):
	mock_exp_item: ExperimentSetItem
	mock_exp: Experiment
	mock_network: Network
	mock_encoding_params: EncodingParameters

	"""
	Sets up some mock experiment data - these can be manipulated as required by the tests
	"""
	@classmethod
	def setUp(cls):
		cls.mock_encoding_params: EncodingParameters = EncodingParameters(
			Video="Beauty",
			Duration="5s",
			Frames_to_Encode=100,
			FPS=30,
			ResWidth=1920,
			ResHeight=1080,
			OutputFile="ID_1_encoded.yuv",
			Encoder="H264",
			EncoderType="Standard",
			Bitrate=45020,
			YuvFormat="4:0:0",
			EncoderMode="RANDOM ACCESS",
			Quality=27,
			Depth=12,
			Gamut="A",
			QPISlice=24,
			QPPSlice=24,
			QPBSlice=24,
			IntraPeriod=1,
			BFrames=2
		)

		cls.mock_exp_item: ExperimentSetItem = ExperimentSetItem(
			SequenceId=1,
			NetworkTopologyId='001',
			networkDisruptionProfileId=10,
			EncodingParameters=cls.mock_encoding_params,
		)

		cls.mock_exp: Experiment = Experiment(
			id="1",
			OwnerId=1,
			experimentName="test_experiment",
			createdAt="",
			description="",
			status="",
			Set=[cls.mock_exp_item]
		)

		cls.mock_network: Network = Network(
			name="test_network",
			id=1,
			packetLoss=9,
			delay=11,
			jitter=11,
			bandwidth=100
		)

	"""
	Ensures the command used to run the video streaming is correct on the golden path
	"""
	def test_virtual_network_driver_command(self):
		net_emu: NetworkEmulator = NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, "/tmp/sample_source.mp4")

		expected_cmd = 'bash /root/ExperimentEngine-Group6/src/network_emulation/virtual-network.sh 1 11 9 /tmp/sample_source.mp4 /tmp/1-1-disrupted.mp4'
		self.assertEqual(net_emu.command, expected_cmd)
	"""
	Ensure that an invalid network topology is rejected properly
	"""
	def test_bad_network_topo(self):
		# Set a network topology id that doesn't exist
		self.mock_exp_item.NetworkTopologyId = '000'

		with self.assertRaises(KnownProcessingException):
			NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, "/tmp/sample_source.mp4")

	"""
	Check that en error is thrown when the source file is missing
	"""
	def test_missing_source_file(self):
		with self.assertRaises(KnownProcessingException):
			_ = NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, "/tmp/non-existent-file.mp4")

	"""
	Tests that a nominal command produces a successful stream
	"""
	@unittest.skipIf(freedesktop_os_release()['ID'] != 'arch', 'Skipping as tests are not being run on Arch linux')
	def test_streaming(self):
		# Set up the network with a test file
		net_emu: NetworkEmulator = NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, "/tmp/sample_source.mp4")
		disrupted_file, streaming_log = net_emu.run()

		self.assertIsNotNone(streaming_log)
		self.assertTrue(exists(disrupted_file))

	"""
	Tests that the demo-mode script command produces a pseudo-successful stream
	"""
	def test_demo_streaming(self):
		# Set the experiment item to be run as a demo network
		self.mock_exp_item.NetworkTopologyId = '999'

		# Remove the result file if needed
		remove("/tmp/1-1-disrupted.mp4")

		expected_output = """[EE_INFO] Sequence_number 1
		[EE_INFO] Delay: 11
		[EE_INFO] Packet Loss: 9
		[EE_INFO] Source file: /tmp/sample_source.mp4
		[EE_INFO] Distorted file path: /tmp/1-1-disrupted.mp4
		[EE_INFO] Enabling sch_netem
		[EE_INFO] Applying network conditions
		[EE_INFO] Deleting previously exported file
		[EE_INFO] Creating sdp file
		[EE_INFO] Starting stream"""

		# Set up the network with a test file
		net_emu: NetworkEmulator = NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, "/tmp/sample_source.mp4")
		streaming_log = net_emu.run()
		self.assertTrue("[EE_INFO] Distorted file path: /tmp/1-1-disrupted.mp4" in streaming_log)
		self.assertTrue(exists(f"/tmp/{self.mock_exp.id}-{self.mock_exp_item.SequenceId}-disrupted.mp4"))

