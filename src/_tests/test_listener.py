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

def processFilesWithUnexpectedError(a: str, b: str, c: int):
    raise Exception("Unknown error")

def processFilesWithKnownError(a: str, b: str, c: int):
    raise KnownProcessingException("id", "Known error", 0, "partner")

def knownErrorCallback(error: KnownProcessingException):
    globals()["knownErrorDetected"] = True

def test_listener_can_process():
    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFiles, knownErrorCallback, 0)

    open(srcPath + "/in/testid1_1_encoded.mp4", "+a").close()

    listener.start(1)

    assert globals()["lastFileId"] == "testid1"
    assert globals()["lastFileName"] == "testid1_1_encoded.mp4"

def test_listener_can_delete():
    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFiles, knownErrorCallback, 0)

    open(srcPath + "/in/testid2_1_encoded.mp4", "+a").close()

    listener.start(1)

    assert os.path.isfile(srcPath + "/in/testid2_1_encoded.mp4") == False

def test_listener_can_handle_known_error():
    globals()["knownErrorDetected"] = False

    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFilesWithKnownError, knownErrorCallback, 0)
    open(srcPath + "/in/testid2_1_encoded.mp4", "+a").close()

    listener.start(1)

    assert globals()["knownErrorDetected"] == True
    assert os.path.isfile(srcPath + "/in/testid2_1_encoded.mp4") == False
    assert os.path.isfile(srcPath + "/in/poison/testid2_1_encoded.mp4") == True
    os.remove(srcPath + "/in/poison/testid2_1_encoded.mp4")

def test_listener_can_handle_unknown_error():
    globals()["knownErrorDetected"] = False

    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFilesWithUnexpectedError, knownErrorCallback, 0)
    open(srcPath + "/in/testid2_1_encoded.mp4", "+a").close()

    listener.start(1)

    assert globals()["knownErrorDetected"] == False
    assert os.path.isfile(srcPath + "/in/testid2_1_encoded.mp4") == False
    assert os.path.isfile(srcPath + "/in/poison/testid2_1_encoded.mp4") == True
    os.remove(srcPath + "/in/poison/testid2_1_encoded.mp4")