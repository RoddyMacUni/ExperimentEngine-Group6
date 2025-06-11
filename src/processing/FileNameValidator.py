from AppSettings import GetAppSettings
import re

class FileNameValidator:
    def ValidateEncodedVideoName(self, fileName: str) -> bool:
        pattern = re.compile(GetAppSettings().EncodedVideoFileNamePattern) #File-Id_1_encoded.mp4 would be valid, for example
        if pattern.fullmatch(fileName):
            return True
        return False