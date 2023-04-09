import pickle
import numpy as np
from typing import Self

from .lineTypeClass import LineType
from .generalMethods import convertToFloat, divideStringArrayFixedWidth

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
        tempElementNumber=tempLines[:,[1]]
        tempElementNumber=tempElementNumber.astype(int)
        
        # Grid coordinates        
        tempValue=tempLines[:,[3,4,5]]
        tempValue=convertToFloat(tempValue)
        
        # Read extra elements
        #print(tempLines.size())
        #if tempLines.shape[1]>5:
        #    pass
        #    tempValue2=tempLines[:,[6:tempLines.shape[1]]]
        #    tempValue2=convertToFloat(tempValue2)           
        
        

        self.elementNumber=tempElementNumber
        self.coordinate=tempElementNumber

        #print(tempValue)
        #print(type(tempLines))
        
        return self
    
def debug():
    file = open('../tempData.dat', 'rb')
    data = pickle.load(file)
    file.close()

if __name__ == "__main__":
    debug()