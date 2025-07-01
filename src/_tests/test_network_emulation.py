from exceptions.KnownProcessingException import KnownProcessingException
from model.Experiment import Experiment, SequenceItem
from model.Network import Network
from network_emulation.NetworkEmulation import NetworkEmulator
import unittest
from platform import freedesktop_os_release
from os.path import exists
from os import remove

TEST_VIDEO_ROOT_DIR = "/root/ExperimentEngine-Group6/test_videos/"

class TestNetworkEmulation(unittest.TestCase):
	mock_exp_item: SequenceItem
	mock_exp: Experiment
	mock_network: Network

	"""
	Sets up some mock experiment data - these can be manipulated as required by the tests
	"""
	@classmethod
	def setUp(cls):
		cls.mock_exp_item: SequenceItem = SequenceItem(
			SequenceId=1,
			NetworkTopologyId=1,
			NetworkDisruptionProfileId=10,
			EncodingParameters=dict(),
		)

		cls.mock_exp: Experiment = Experiment(
			Id=1,
			OwnerId=1,
			ExperimentName="test_experiment",
			CreatedAt="",
			Description="",
			status="",
			Sequences=[cls.mock_exp_item]
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
	@unittest.skipIf(freedesktop_os_release()['ID'] != 'arch', 'Skipping as tests are not being run on Arch linux')
	def test_virtual_network_driver_command(self):
		net_emu: NetworkEmulator = NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, TEST_VIDEO_ROOT_DIR + "sample_source.mp4")

		expected_cmd = f'bash /root/ExperimentEngine-Group6/src/network_emulation/virtual-network.sh 1 11 9 {TEST_VIDEO_ROOT_DIR}sample_source.mp4 {TEST_VIDEO_ROOT_DIR}1-1-disrupted.mp4'
		self.assertEqual(net_emu.command, expected_cmd)
	"""
	Ensure that an invalid network topology is rejected properly
	"""
	def test_bad_network_topo(self):
		# Set a network topology id that doesn't exist
		self.mock_exp_item.NetworkTopologyId = 0

		with self.assertRaises(KnownProcessingException):
			NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, f"{TEST_VIDEO_ROOT_DIR}sample_source.mp4")

	"""
	Check that en error is thrown when the source file is missing
	"""
	def test_missing_source_file(self):
		with self.assertRaises(KnownProcessingException):
			_ = NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, f"{TEST_VIDEO_ROOT_DIR}non-existent-file.mp4")

	"""
	Tests that a nominal command produces a successful stream
	"""
	@unittest.skipIf(freedesktop_os_release()['ID'] != 'arch', 'Skipping as tests are not being run on Arch linux')
	def test_streaming(self):
		# Set up the network with a test file
		net_emu: NetworkEmulator = NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, f"{TEST_VIDEO_ROOT_DIR}sample_source.mp4")
		disrupted_file, streaming_log = net_emu.run()

		self.assertIsNotNone(streaming_log)
		self.assertTrue(exists(disrupted_file))

	"""
	Tests that the demo-mode script command produces a pseudo-successful stream
	"""
	@unittest.skipIf(freedesktop_os_release()['ID'] != 'arch', 'Skipping as tests are not being run on Arch linux')
	def test_demo_streaming(self):
		# Set the experiment item to be run as a demo network
		self.mock_exp_item.NetworkTopologyId = 999

		# Set up the network with a test file
		net_emu: NetworkEmulator = NetworkEmulator(self.mock_exp_item, self.mock_exp, self.mock_network, f"{TEST_VIDEO_ROOT_DIR}sample_source.mp4")
		streaming_log = net_emu.run()
		self.assertIsNotNone(streaming_log)
		self.assertTrue(exists(f"{TEST_VIDEO_ROOT_DIR}{self.mock_exp.Id}-{self.mock_exp_item.SequenceId}-disrupted.mp4"))

		# Remove the result file if needed
		remove(f"{TEST_VIDEO_ROOT_DIR}1-1-disrupted.mp4")