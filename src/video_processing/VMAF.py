import re
import subprocess
import shlex


class VMAFEvaluator:
    def __init__(self, reference_path, distorted_path, ffmpeg_path="ffmpeg"):
        self.reference_path = reference_path
        self.distorted_path = distorted_path
        self.ffmpeg_path = ffmpeg_path


    def evaluate(self):
        cmd = (
            f'ffmpeg -i "{self.distorted_path}" -i "{self.reference_path}" '
            '-lavfi libvmaf '
            '-f null -'  # discard rendered video
        )

        try:
            proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True, check=True)

            match = re.search("VMAF score:\s*([0-9]+(?:\.[0-9]+)?)\s*", proc.stderr)
            if match:
                return float(match.group(1))
            else:
                raise ValueError("VMAF score not found in ffmpeg output")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"ffmpeg error: {e.stderr}") from e
