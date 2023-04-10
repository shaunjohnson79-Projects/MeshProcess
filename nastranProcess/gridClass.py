import pickle
import numpy as np
from typing import Self
from dataclasses import dataclass
from pytictoc import TicToc

from .lineTypeClass import LineType
from .generalMethods import convertToFloat,convertToInt
from .generalMethods import divideStringArrayFixedWidth


class Grid():
    def __init__(self,rawData) -> None:
        #print("Grid init")
        self.pointer = np.ndarray
        self.coordinate = np.ndarray
        
        self.convert(rawData)
        
    def __repr__(self):
        # returnString = ''
        # returnString += f"{self.coordinate.shape}"
        # #returnString += f"\n"
        # return returnString
    
        returnString = ''
        tempDict=self.__dict__
        for key in tempDict:
            returnString += f"{key}: {tempDict[key].shape}\n"
        return returnString
        
    def convert(self,rawData) -> Self:
        """Convert the rawData"""
        
        # Start timer
        timer = TicToc() 
        timer.tic()
        
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
        
        timer.toc("Convert Grid:")
        return self
