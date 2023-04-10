from pytictoc import TicToc
from typing import Self
import numpy as np
from dataclasses import dataclass

from .lineTypeClass import LineType

@dataclass
class RawData():
    def __init__(self) -> None:
        self.data: np.array


        
    def read(self,fileName) -> Self:
        """Read in the raw data"""
        
        # Start timer
        timer = TicToc()
        timer.tic()
        
        with open(fileName) as fileHandle:
            Lines = fileHandle.readlines()
        self.data=np.array(Lines)
        
        # Remove new line charcter from strings
        self.data=np.core.defchararray.replace(self.data,"\n",'', count=None)
        
        timer.toc("Read Raw Data:")

        return self
    
    def display(self) -> None:
        print(self.data)
        
    @property
    def numberOfLines(self) -> int:
        """Get the number of lines in the file"""
        return len(self.data)
    
    def CountEnumType(self,enumType) -> int:
        return np.count_nonzero(self.getLineTypes == enumType)
    
    @property
    def getLineTypes(self) -> list:
        """Make a list of the LineTypes"""

        # Check if variable has already been calculated
        if hasattr(self,'lineTypeList'):
            return self.lineTypeList
        
        # define the list
        self.lineTypeList = np.empty(self.numberOfLines,dtype=LineType)
        
        # fill the list
        for i, line in np.ndenumerate(self.data):
            self.lineTypeList[i]=self.getLineType(line)  
                   
        return self.lineTypeList
                      
    def getLineType(self,line) -> LineType:
        """get the line Type"""
        if line.startswith(LineType.GRID.value):
            return LineType.GRID
        elif line.startswith(LineType.BEGINBULK.value):
            return LineType.BEGINBULK
        elif line.startswith(LineType.COMMENT.value):
            return LineType.COMMENT
        elif line.startswith(LineType.SOL.value):
            return LineType.SOL
        elif line.startswith(LineType.CEND.value):
            return LineType.CEND
        elif line.startswith(LineType.PSOLID.value):
            return LineType.PSOLID
        elif line.startswith(LineType.CTETRA.value):
            return LineType.CTETRA
        elif line.startswith(LineType.CPENTA.value):
            return LineType.CPENTA
        elif line.startswith(LineType.EIGRL.value):
            return LineType.EIGRL  
        elif line.startswith(LineType.ENDDATA.value):
            return LineType.ENDDATA      
        else:
            print("Unknown line")
            print(line)
            return