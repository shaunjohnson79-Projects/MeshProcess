#from .rawDataClass import RawData
from pytictoc import TicToc
import numpy as np

class ReadFile():
    
    def __init__(self, fileName) -> None:
        print("read nastran from file")
        self.fileName = fileName
        
        self.rawData = RawData().read(fileName)
       
        print(self.rawData.blah())
        print(self.rawData.numberOfLines)
        

class RawData():
    def __init__(self) -> None:
        print("raw Data init")
         
    def read(self, fileName):
        """Read in the raw data"""
        
        timer = TicToc() #create instance of class
        timer.tic()
        
        with open(fileName) as fileHandle:
            Lines = fileHandle.readlines()
        self.data = np.array(Lines)
        
        # Remove new line character from strings
        self.data = np.core.defchararray.replace(self.data,"\n",'', count=None)
        
        timer.toc("Read Raw Data:")
        
        return self
    
    def blah(self) -> None:
        print(self.data)
    

    @property
    def numberOfLines(self) -> int:
        """Get the number of lines in the file"""
        return len(self.data)
    
def main():
    print("main: start")
    fileName = "nastran_input.nas"
    
    nastranData = ReadFile(fileName)
    
    print("main: end")


if __name__ == "__main__":
    main()
