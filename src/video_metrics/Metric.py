import re
import subprocess
import shlex


class VMAFEvaluator:
    def __init__(self, reference_path: str, distorted_path: str):
        self.reference_path = reference_path
        self.distorted_path = distorted_path


    def evaluate(self) -> tuple[str, str, str]:
        cmd = "ffmpeg -i " + \
              self.distorted_path + \
              " -i " + self.reference_path + \
              ' -lavfi "[0:v][1:v]libvmaf,[0:v][1:v]psnr,[0:v][1:v]ssim"' + \
              " -f null -"

        try:
            proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True, check=True)

            vmaf_regex = re.search(r'VMAF score:\s*([0-9]+(?:\.[0-9]+)?)', proc.stderr).group(1)
            ssim_regex = re.search(r'(?mi)^.*SSIM.*?All:\s*([^\r\n]*)', proc.stderr).group(1)
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

        return vmaf, ssim, psnr