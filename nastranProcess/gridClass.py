import pickle
import numpy as np
from typing import Self

from .lineTypeClass import LineType
from .generalMethods import convertToFloat,convertToInt
from .generalMethods import divideStringArrayFixedWidth

class Grid():
    def __init__(self) -> None:
        print("Grid init")
        
    def convert(self,rawData) -> Self:
        # Get the grid lines
        tempLines = rawData.data[rawData.getLineTypes == LineType.GRID]
        
        # Divide the lines by fixed width
        width=8
        tempLines=divideStringArrayFixedWidth(tempLines,width)
        
        # Element Numbers
        self.pointer=tempLines[:,[1]]
        self.pointer=convertToInt(self.pointer)
        
        # Grid coordinates        
        self.coordinate=tempLines[:,[3,4,5]]
        self.coordinate=convertToFloat(self.coordinate)
        
        # Read extra elements
        if tempLines.shape[1]>5:
            self.extra=tempLines[:,6:]
            self.extra=convertToInt(self.extra)  
            
        #print(tempValue)
        #print(type(tempLines))
        
        return self
    
def debug():
    file = open('../tempData.dat', 'rb')
    data = pickle.load(file)
    file.close()

if __name__ == "__main__":
    debug()