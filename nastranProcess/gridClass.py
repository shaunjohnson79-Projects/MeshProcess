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
        
        # Grid coordinates        
        tempValue=tempLines[:,[3,4,5]]
        tempValue=convertToFloat(tempValue)
        
        # Element Numbers
        tempElementNumber=tempLines[:,[1]]
        tempElementNumber=tempElementNumber.astype(int)

        self.elementNumber=tempElementNumber
        self.coordinate=tempElementNumber

        print(tempValue)
        print(type(tempLines))
        
        return self
