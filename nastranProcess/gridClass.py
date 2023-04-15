import numpy as np
from typing import Self
from dataclasses import dataclass
from pytictoc import TicToc

from .lineTypeClass import LineType
from .generalMethods import convertToFloat, convertToInt
from .generalMethods import divideStringArrayFixedWidth
from .generalMethods import divideEnumType


class Grid():
    def __init__(self, rawData) -> None:
        # print("Grid init")
        self.pointer = np.ndarray
        self.coordinate = np.ndarray

        tempLineType = LineType.GRID

        self.convert(rawData, tempLineType)

    def __repr__(self):
        # returnString = ''
        # returnString += f"{self.coordinate.shape}"
        # #returnString += f"\n"
        # return returnString

        returnString = ''
        tempDict = self.__dict__
        for key in tempDict:
            returnString += f"{key}: {tempDict[key].shape}\n"
        return returnString

    def convert(self, rawData, tempLineType) -> Self:
        """Convert the rawData"""

        # Start timer
        timer = TicToc()
        timer.tic()

        # Divide the lines by fixed width
        tempLines = divideEnumType(rawData, tempLineType)

        # Element Numbers
        self.pointer = tempLines[:, [0]]
        self.pointer = convertToInt(self.pointer)

        # Grid coordinates
        self.coordinate = tempLines[:, [2, 3, 4]]
        self.coordinate = convertToFloat(self.coordinate)

        # Read extra elements
        if tempLines.shape[1] > 4:
            self.extra = tempLines[:, 5:]
            self.extra = convertToInt(self.extra)

        timer.toc(
            f"Convert: {tempLineType.value}={rawData.CountEnumType(tempLineType)}: ")
        return self
