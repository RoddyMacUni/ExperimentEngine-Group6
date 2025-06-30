import re
import subprocess
import shlex


class MetricEvaluator:

    def evaluate(reference_path: str, distorted_path: str) -> tuple[float,  float, float]:
        cmd = "ffmpeg -i " + \
              distorted_path + \
              " -i " + reference_path + \
              ' -lavfi "[0:v][1:v]libvmaf,[0:v][1:v]psnr,[0:v][1:v]ssim"' + \
              " -f null -"

        try:
            proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True, check=True)

            vmaf_regex = re.search(r'VMAF score:\s*([0-9]+(?:\.[0-9]+)?)', proc.stderr).group(1)
            ssim_regex = re.search(r'(?mi)^.*SSIM.*?All:\s*([0-9.]+)', proc.stderr).group(1)
            psnr_regex = re.search(r'(?mi)^.*PSNR.*?\saverage:\s*(inf|\d+(?:\.\d+)?)', proc.stderr).group(1)

            if vmaf_regex and ssim_regex and psnr_regex:
                vmaf = str(vmaf_regex)
                ssim = ssim_regex
                psnr = psnr_regex
            else:
                raise ValueError("VMAF, SSIM or PSNR score not found in ffmpeg output")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"ffmpeg error: {e.stderr}") from e

        if "inf" in ssim:
            ssim = "1.0"

        if psnr == "inf":
            psnr = "9999.0"

        return float(vmaf), float(ssim), float(psnr)

    def evaluateBitRate(ffmpeg_output: str) -> float:
        bitrate_regex = re.search(r'bitrate=\s*([0-9]+(?:\.[0-9]+)?)kbits/s', ffmpeg_output)

        if bitrate_regex:
            bitrate = float(bitrate_regex.group(1))
        else:
            raise ValueError("Failed to get bitrate from " + ffmpeg_output)

        return bitrate