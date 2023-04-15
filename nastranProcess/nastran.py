import numpy as np

from pytictoc import TicToc
from dataclasses import dataclass

from .rawDataClass import RawData
from .gridClass import Grid
from .meshClass import Mesh
from .commentClass import Comment, CommentRaw
from .pshellClass import Pshell, PshellRaw
from .cord2RClass import Cord2r, Cord2rRaw
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
        # self.getGridData()
        # self.getMeshData()
        # self.getPshellData()
        # self.getCord2rData()
        self.getCommentData()

        # Stop timer
        timer.toc("Read Nastran File:")

    def getRawData(self, fileName) -> None:
        """Read in the rawData"""

        self.rawData = RawData(fileName)

        # print(self.rawData.display())
        # print(self.rawData.numberOfLines)
        # print(self.rawData.CountEnumType(LineType.GRID))

    def containsEnum(self, tempEnum) -> bool:
        if self.rawData.CountEnumType(tempEnum) == 0:
            return False
        else:
            return True

    """-------------------------------------------"""
    """-------------------------------------------"""
    """-------------------------------------------"""

    def getGridData(self) -> None:
        """Get Grid"""

        if not self.containsEnum(LineType.GRID):
            return

        self.grid = Grid(self.rawData)

        self.rawData.deleteEnumType(LineType.GRID)

    def getMeshData(self) -> None:
        """Get Mesh dictionary for the different sort of connectors"""

        self.mesh = {}

        for MNOEP in MeshNOE:
            lineTypeHandle = getEnum(MNOEP.name, LineType)
            meshNOEHandle = getEnum(MNOEP.name, MeshNOE)

            if (lineTypeHandle == None) or (meshNOEHandle == None):
                continue

            if not self.containsEnum(lineTypeHandle):
                continue

            self.mesh[str(MNOEP.name)] = Mesh(
                self.rawData, lineTypeHandle, meshNOEHandle)

            self.rawData.deleteEnumType(lineTypeHandle)

    def getPshellData(self) -> None:
        """Get Pshell"""

        if not self.containsEnum(LineType.PSHELL):
            return

        # Create an empty dictionary to store the rows
        self.pshell = {}

        pShellRaw = PshellRaw(self.rawData)

        # Loop over each row in the array
        for i in range(pShellRaw.rawData.shape[0]):
            tempData = Pshell(pShellRaw.rawData[i])
            tempName = tempData.value
            self.pshell[tempName] = tempData

            print(f"\tPshell: {tempName}")

        self.rawData.deleteEnumType(LineType.PSHELL)

    def getCord2rData(self) -> None:
        """Get Cord2R"""

        # Create an empty dictionary to store the rows
        self.cord2r = {}

        if not self.containsEnum(LineType.CORD2R):
            return

        cord2rRaw = Cord2rRaw(self.rawData)

        # Loop over each row in the array
        for i in range(cord2rRaw.rawData.shape[0]):
            tempData = Cord2r(cord2rRaw.rawData[i])
            tempName = tempData.value
            self.cord2r[tempName] = tempData

            print(f"\tCord2r: {tempName}")

        self.rawData.deleteEnumType(LineType.CORD2R)

    def getCommentData(self) -> None:
        """Get Comment"""

        if not self.containsEnum(LineType.COMMENT):
            return

        commentRaw = CommentRaw(self.rawData)

        self.rawData.deleteEnumType(LineType.COMMENT)
