import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from processing.DirectoryListener import DirectoryListener


global lastFile
global lastFileName
def processFiles(a: str, b: str):
    globals()["lastFile"] = a
    globals()["lastFileName"] = b

def test_listener_can_process():
    listener = DirectoryListener("./../in", ["README.md"], processFiles)

    open("./../in/test1.txt", "+a").close()

    listener.start(1)

    assert lastFile == "test1.txt"
    assert lastFileName == "test1"

def test_listener_can_delete():
    listener = DirectoryListener("./../in", ["README.md"], processFiles)

    open("./../in/test2.txt", "+a").close()

    listener.start(1)

    assert os.path.isfile("./../in/test2.txt") == False