import os
import sys

#Add src to PATH
srcPath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(srcPath)

from processing.DirectoryListener import DirectoryListener
from exceptions.KnownProcessingException import KnownProcessingException


global lastFile
global lastFileName
def processFiles(a: str, b: str, c: int):
    globals()["lastFileId"] = a
    globals()["lastFileName"] = b

def knownErrorCallback(error: KnownProcessingException):
    pass

def test_listener_can_process():
    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFiles, knownErrorCallback)

    open(srcPath + "/in/testid1_1_encoded.mp4", "+a").close()

    listener.start(1)

    assert globals()["lastFileId"] == "testid1"
    assert globals()["lastFileName"] == "testid1_1_encoded.mp4"

def test_listener_can_delete():
    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFiles, knownErrorCallback)

    open(srcPath + "/in/testid2_1_encoded.mp4", "+a").close()

    listener.start(1)

    assert os.path.isfile(srcPath + "/in/testid2_1_encoded.mp4") == False