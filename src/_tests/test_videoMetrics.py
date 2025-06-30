import unittest
from video_metrics.Metric import MetricEvaluator
import sys

from vmaf.python import vmaf

REF_PATH = "../../test_videos/sample_source.mp4"
DIS_PATH = "../../test_videos/sample_degraded.mp4"
DIF_PATH = "../../test_videos/sample_different.mp4"


def file_to_string(param):
    with open(param, "r") as f:
        file_content = f.read()
        return file_content

@unittest.skipUnless(
    sys.platform.startswith("win"),
    "Custom FFmpeg build currently only runs on windows"
)
class MyTestCase(unittest.TestCase):

    def test_sameVideo(self):

        vmaf, ssim, psnr = MetricEvaluator.evaluate(reference_path=REF_PATH, distorted_path=REF_PATH)

        self.assertGreater(vmaf, 95.0) #96 is a high VMAF score -> identical videos
        self.assertEqual(ssim, 1.0)
        self.assertEqual(psnr, 9999.0)

    def test_DegradedVideo(self):

        vmaf, ssim, psnr = MetricEvaluator.evaluate(reference_path=REF_PATH, distorted_path=DIS_PATH)

        self.assertGreater(vmaf, 90.0) #96 is a high VMAF score -> identical videos
        self.assertEqual(ssim, 0.983802)
        self.assertEqual(psnr, 42.773112)

    def test_DifferentVideo(self):

        vmaf, ssim, psnr = MetricEvaluator.evaluate(reference_path=REF_PATH, distorted_path=DIF_PATH)

        self.assertEqual(vmaf, 0.0) # Should be 0 completely different videos
        self.assertLess(ssim, 0.5) # should be low value
        self.assertLess(psnr, 20) # Fairly low value

    def test_bitrate(self):

        example_command_line_output = file_to_string("../../test_videos/sample_bitrate_output_1.txt")

        self.assertEqual(MetricEvaluator.evaluateBitRate(example_command_line_output), 517.7)


if __name__ == '__main__':
    unittest.main()
