from processing.Counter import Counter
import os
import time
from typing import Callable
import re

class DirectoryListener:
    targetFolder: str
    ignoreFiles: list[str]
    processorFunction: Callable[[str, str], None] #takes the file name and name without any file extensions

    stopFlag: bool = False

    def __init__(self, targetFolder: str, ignoreFiles: list[str], processorFunction: Callable[[str, str], None]):
        self.targetFolder = targetFolder
        self.ignoreFiles = ignoreFiles
        self.processorFunction = processorFunction

        self.ignoreFiles.append("poison")

    #Start the listener, TODO this could probably be asyncronous
    #Can set a limit to to the number of loops for testing
    #Includes a counter to give some output while inactive
    def start(self, stopAfter: int = -1):
        print("Listening for file on " + self.targetFolder)

        #Create folder for failed files
        if not os.path.exists(self.targetFolder + "/poison"):
            os.makedirs(self.targetFolder + "/poison")

        counter = Counter(60, lambda minutes: print("No new file detected for " + str(minutes) + " minutes."))
        
        while not self.stopFlag and (stopAfter < 0 or counter.total < stopAfter):
            files = sorted(os.listdir(self.targetFolder), key=lambda filename: os.path.getmtime(self.targetFolder + "/" + filename), reverse=False)

            #Ignore specified files
            for i in range(len(self.ignoreFiles)):
                files.remove(self.ignoreFiles[i])

            if len(files) > 0:
                counter.reset()
                print("File detected: " + files[0])

                pattern = re.compile("[A-Za-z0-9-]+_encoded.mp4") #File-Id_encoded.mp4 would be valid, for example
                if not pattern.fullmatch(files[0]):
                    print("File name did not follow expected pattern, moving to poison queue")
                    os.rename(self.targetFolder + "/" + files[0], self.targetFolder + "/poison/" + files[0])
                    continue

                self.processorFunction(files[0].partition('.')[0].partition('_')[0], files[0]) #File id only, file full name

                os.remove(self.targetFolder + "/" + files[0])
            else:
                time.sleep(1)
                counter.increment()

    #Set stop flag for listener
    def stop(self):
        self.stopFlag = True