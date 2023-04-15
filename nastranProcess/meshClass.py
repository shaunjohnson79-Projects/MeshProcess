import numpy as np
from typing import Self
from dataclasses import dataclass
from pytictoc import TicToc

from .lineTypeClass import LineType, MeshNOE
from .generalMethods import convertToInt
from .generalMethods import divideStringArrayFixedWidth, getEnum
from .generalMethods import divideEnumType


class Mesh():
    def __init__(self, rawData, lineTypeHandle, meshNOEHandle) -> None:
        self.pointer = np.array
        self.tempElementNumber = np.array
        self.mesh = np.array
        self.lineType = lineTypeHandle
        self.meshNOE = meshNOEHandle
        self.name = str(lineTypeHandle.value)

        self.convert(rawData)

    def __repr__(self):
        pass
        # returnString = ''
        # tempDict=self.__dict__
        # for key in tempDict:
        #     tempValue=tempDict[key]
        #     returnString += f"{key}: {tempValue}\n"
        # return returnString

    def convert(self, rawData) -> Self:
        # Start timer
        timer = TicToc()
        timer.tic()

        # Divide the lines by fixed width
        tempLines = divideEnumType(rawData, self.lineType)

        # Pointer
        self.pointer = tempLines[:, [0]]
        self.pointer = convertToInt(self.pointer)

        # elementNumber??
        self.pshell = tempLines[:, [1]]
        self.pshell = convertToInt(self.pshell)

        # Mesh
        self.mesh = tempLines[:, 2:]
        self.mesh = convertToInt(self.mesh)
        self.mesh = self.mesh[:, :int(self.meshNOE.value)]

        timer.toc(
            f"Convert: {self.name}={rawData.CountEnumType(self.lineType)}:")
