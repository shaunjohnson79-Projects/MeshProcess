import numpy as np
from typing import Self
from dataclasses import dataclass
from pytictoc import TicToc

from .lineTypeClass import LineType
from .generalMethods import convertToFloat, convertToInt
from .generalMethods import divideEnumType


class Pshell():
    def __init__(self, rawData) -> None:
        # print("Pshell Init")
        self.array = np.ndarray
        self.value = int

        self.convert(rawData)

    def convert(self, rawData) -> Self:
        self.array = rawData
        self.value = rawData[0]


class PshellRaw():
    def __init__(self, rawData) -> None:
        # print("Pshell Init")
        self.rawData = np.ndarray

        self.convert(rawData)

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

    def convert(self, rawData) -> Self:
        """Convert the rawData"""

        tempLineType = LineType.PSHELL

        # Start timer
        timer = TicToc()
        timer.tic()

        # Divide the lines by fixed width
        tempLines = divideEnumType(rawData, tempLineType)

        # get the rawData
        self.rawData = tempLines
        self.rawData = convertToInt(self.rawData)

        # print(self.pshell)

        timer.toc(
            f"Convert: {tempLineType.value}={rawData.CountEnumType(tempLineType)}: ")
        return self
