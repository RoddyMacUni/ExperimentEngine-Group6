from AppSettings import AppSettings, GetAppSettings
from exceptions.KnownProcessingException import KnownProcessingException
from processing.Counter import Counter
from processing.FileNameValidator import FileNameValidator
import os
import time
from typing import Callable
import re

class DirectoryListener:
    targetFolder: str
    ignoreFiles: list[str]
    processorFunction: Callable[[str, str], None] #takes the file name and name without any file extensions
    errorHandlerFunction: Callable[[KnownProcessingException], None] #takes and handles a known processing exception

    stopFlag: bool = False

    def __init__(self, targetFolder: str, ignoreFiles: list[str], processorFunction: Callable[[str, str], None], errorHandlerFunction: Callable[[KnownProcessingException], None]):
        self.targetFolder = targetFolder
        self.ignoreFiles = ignoreFiles
        self.processorFunction = processorFunction
        self.errorHandlerFunction = errorHandlerFunction

        self.ignoreFiles.append("poison")

        #Create folder for failed files
        #TODO we may want an auto-clearing policy for this, very low priority though
        if not os.path.exists(self.targetFolder + "/poison"):
            os.makedirs(self.targetFolder + "/poison")

    def moveToPoison(self, filename: str):
        os.rename(self.targetFolder + "/" + filename, self.targetFolder + "/poison/" + filename)

    #Start the listener, TODO this could probably be asyncronous
    #Can set a limit to to the number of loops for testing
    #Includes a counter to give some output while inactive
    def start(self, stopAfter: int = -1):
        print("Listening for file on " + self.targetFolder)

        counter = Counter(60, lambda minutes: print("No new file detected for " + str(minutes) + " minutes."))
        
        while not self.stopFlag and (stopAfter < 0 or counter.total < stopAfter):
            files = sorted(os.listdir(self.targetFolder), key=lambda filename: os.path.getmtime(self.targetFolder + "/" + filename), reverse=False)

            #Ignore specified files
            for i in range(len(self.ignoreFiles)):
                if self.ignoreFiles[i] in files:
                    files.remove(self.ignoreFiles[i])

            if len(files) > 0:
                counter.reset()
                print("File detected: " + files[0])

                if not FileNameValidator().ValidateEncodedVideoName(files[0]):
                    print("File name did not follow expected pattern, moving to poison queue")
                    self.moveToPoison(files[0])
                    continue

                #We definitly want this top level error handling to stop the process ending undexpectedly
                #Inside the processing if an error is handled we want to:
                #    1.Send the specific error to results (TODO implement that here too?)
                #    2.Throw an error so it is caught here and the poison item is removed from the main queue
                #TODO would also be worth implementing something that will also check for files appearing 
                # multiple times in a row as a fallback
                try:
                    fileId = files[0].partition('.')[0].partition('_')[0]
                    fileName = files[0]
                    sequenceNumber = files[0].partition('.')[0].partition('_')[2].partition('_')[0]
                    self.processorFunction(fileId, fileName, sequenceNumber)
                except KnownProcessingException as e:
                    print("An error has occurred during processing: " + e.message)
                    self.moveToPoison(files[0])
                    self.errorHandlerFunction(e)
                except Exception as e:
                    print("An unknown error occurred during processing: ")
                    print(e)
                    self.moveToPoison(files[0])
                else: 
                    os.remove(self.targetFolder + "/" + files[0])
            else:
                time.sleep(1)
                counter.increment()

    #Set stop flag for listener
    def stop(self):
        self.stopFlag = True