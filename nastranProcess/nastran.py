from pytictoc import TicToc
from dataclasses import dataclass

from .rawDataClass import RawData
from .gridClass import Grid
from .meshClass import Mesh
from .lineTypeClass import LineType, MeshNOE
from .generalMethods import getEnum


# @dataclass()
class Nastran:
    def __init__(self) -> None:
        # define variables
        self.fileName = str
        self.precision = 8
        self.isGood = False

    def __repr__(self):
        returnString = ''
        tempDict = self.__dict__
        for key in tempDict:
            returnString += f"{key}: {tempDict[key]}\n"
        return returnString

    def readfromFile(self, fileName) -> None:
        """Read the file data"""

        # Add the filename to the class
        self.fileName = fileName

        # Start timer
        timer = TicToc()
        timer.tic()

        # Read in the rawData from the file
        self.getRawData(fileName)

        # Process the rawData
        self.getGridData(self.rawData)
        self.getMeshData(self.rawData)

        # Stop timer
        timer.toc("Read Nastran File:")

    def getRawData(self, fileName) -> None:
        """Read in the rawData"""

        self.rawData = RawData(fileName)

        # print(self.rawData.display())
        # print(self.rawData.numberOfLines)
        # print(self.rawData.CountEnumType(LineType.GRID))

    def getGridData(self, rawData) -> None:
        """Get Grid"""

        self.grid = Grid(rawData)

    def getMeshData(self, rawData) -> None:
        """Get Mesh dictionary for the different sort of connectors"""

        self.mesh = {}

        for MNOEP in MeshNOE:
            lineTypeHandle = getEnum(MNOEP.name, LineType)
            meshNOEHandle = getEnum(MNOEP.name, MeshNOE)

            if (lineTypeHandle == None) or (meshNOEHandle == None):
                continue

            if rawData.CountEnumType(lineTypeHandle) == 0:
                continue

            self.mesh[str(MNOEP.name)] = Mesh(
                rawData, lineTypeHandle, meshNOEHandle)
