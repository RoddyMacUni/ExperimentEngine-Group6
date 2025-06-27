# import unittest
# from video_metrics.Metric import VMAFEvaluator
# import sys

# REF_PATH = "../../test_videos/sample_source.mp4"
# DIS_PATH = "../../test_videos/sample_degraded.mp4"
# DIF_PATH = "../../test_videos/sample_different.mp4"

# @unittest.skipUnless(
#     sys.platform.startswith("win"),
#     "Custom FFmpeg build currently only runs on windows"
# )
# class MyTestCase(unittest.TestCase):

#     def test_sameVideo(self):

#         test_harness = VMAFEvaluator(reference_path=REF_PATH, distorted_path=REF_PATH)

#         vmaf, ssim, psnr = test_harness.evaluate()

#         self.assertGreater(float(vmaf), 95.0) #96 is a high VMAF score -> identical videos
#         self.assertEqual(float(ssim), 1.0)
#         self.assertEqual(psnr, "inf")

#     def test_DegradedVideo(self):
#         test_harness = VMAFEvaluator(reference_path=REF_PATH, distorted_path=DIS_PATH)

#         vmaf, ssim, psnr = test_harness.evaluate()

#         self.assertGreater(float(vmaf), 90.0) #96 is a high VMAF score -> identical videos
#         self.assertEqual(float(ssim), 0.983802)
#         self.assertEqual(float(psnr), 42.773112)

#     def test_DifferentVideo(self):
#         test_harness = VMAFEvaluator(reference_path=REF_PATH, distorted_path=DIF_PATH)

#         vmaf, ssim, psnr = test_harness.evaluate()

#         self.assertEqual(float(vmaf), 0.0) # Should be 0 completely different videos
#         self.assertLess(float(ssim), 0.5) # should be low value
#         self.assertLess(float(psnr), 20) # Fairly low value


# if __name__ == '__main__':
#     unittest.main()
