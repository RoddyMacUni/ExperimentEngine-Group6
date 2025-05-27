import os
import sys

#Add src to PATH
srcPath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(srcPath)

from processing.DirectoryListener import DirectoryListener


global lastFile
global lastFileName
def processFiles(a: str, b: str):
    globals()["lastFileId"] = a
    globals()["lastFileName"] = b

def test_listener_can_process():
    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFiles)

    open(srcPath + "/in/testid1_encoded.txt", "+a").close()

    listener.start(1)

    assert globals()["lastFileId"] == "testid1"
    assert globals()["lastFileName"] == "testid1_encoded.txt"

def test_listener_can_delete():
    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFiles)

    open(srcPath + "/in/testid2_encoded.txt", "+a").close()

    listener.start(1)

    assert os.path.isfile(srcPath + "/in/testid2_encoded.txt") == False