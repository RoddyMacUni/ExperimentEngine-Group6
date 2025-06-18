import unittest
from video_metrics.Metric import VMAFEvaluator

REF_PATH = "../../test_videos/sample_source.mp4"
DIS_PATH = "../../test_videos/sample_source.mp4"

class MyTestCase(unittest.TestCase):

    def test_sameVideo(self):
        test_harness = VMAFEvaluator(reference_path=REF_PATH, distorted_path=REF_PATH)

        vmaf, ssim, psnr = test_harness.evaluate()

        self.assertGreater(float(vmaf), 95.0) #96 is a high VMAF score -> identical videos
        self.assertEqual(float(ssim), 1.0)
        self.assertEqual(psnr, "inf")

    def test_DifferentVideo(self):
        test_harness = VMAFEvaluator(reference_path=REF_PATH, distorted_path=DIS_PATH)

        vmaf, ssim, psnr = test_harness.evaluate()

        self.assertGreater(float(vmaf), 95.0) #96 is a high VMAF score -> identical videos
        self.assertEqual(float(ssim), 1.0)
        self.assertEqual(psnr, "inf")


if __name__ == '__main__':
    unittest.main()
