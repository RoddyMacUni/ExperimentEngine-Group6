import os
import sys

srcPath: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(srcPath)

from processing.DirectoryListener import DirectoryListener


global lastFile
global lastFileName
def processFiles(a: str, b: str):
    globals()["lastFile"] = a
    globals()["lastFileName"] = b

def test_listener_can_process():
    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFiles)

    open(srcPath + "/in/test1.txt", "+a").close()

    listener.start(1)

    assert globals()["lastFile"] == "test1.txt"
    assert globals()["lastFileName"] == "test1"

def test_listener_can_delete():
    listener = DirectoryListener(srcPath + "/in", ["README.md"], processFiles)

    open(srcPath + "/in/test2.txt", "+a").close()

    listener.start(1)

    assert os.path.isfile(srcPath + "/in/test2.txt") == False