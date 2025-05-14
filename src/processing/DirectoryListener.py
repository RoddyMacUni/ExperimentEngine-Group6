from processing.Counter import Counter
import os
import time
from typing import Callable

class DirectoryListener:
    targetFolder: str
    ignoreFiles: list[str]
    processorFunction: Callable[[str, str], None] #takes the file name and name without any file extensions

    stopFlag: bool = False

    def __init__(self, targetFolder: str, ignoreFiles: list[str], processorFunction: Callable[[str, str], None]):
        self.targetFolder = targetFolder
        self.ignoreFiles = ignoreFiles
        self.processorFunction = processorFunction

    def start(self, stopAfter: int = -1):
        print("Listening for file on " + self.targetFolder)
        counter = Counter(60, lambda minutes: print("No new file detected for " + str(minutes) + " minutes."))
        while not self.stopFlag and (stopAfter < 0 or counter.total < stopAfter):
            files = sorted(os.listdir(self.targetFolder), key=lambda filename: os.path.getmtime(self.targetFolder + "/" + filename), reverse=False)
            for i in range(len(self.ignoreFiles)):
                files.remove(self.ignoreFiles[i])

            if len(files) > 0:
                counter.reset()
                print("File detected: " + files[0])

                self.processorFunction(files[0], files[0].partition('.')[0]) #Remove file extension

                os.remove(self.targetFolder + "/" + files[0])
            else:
                time.sleep(1)
                counter.increment()

    def stop(self):
        self.stopFlag = True