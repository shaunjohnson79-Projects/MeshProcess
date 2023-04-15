from pytictoc import TicToc
from typing import Self
import numpy as np
from dataclasses import dataclass
import os
import re

try:
    from .lineTypeClass import LineType
except:
    # Debug Mode
    from lineTypeClass import LineType


class RawData():
    def __init__(self, fileName) -> None:
        self.data = np.array

        # Start timer
        timer = TicToc()
        timer.tic()

        self.read(fileName)

        # Combine Long lines
        self.combineLines(LineType.PLUS)
        self.combineLines(LineType.STAR)

        # remove getLineTypes as the lines have changed
        # del self.getLineTypes
        # self.getLineTypes

        # End timer
        timer.toc("Read Raw Data:")

    def combineLines(self, EnumLineType):
        """Combine lines that have a certain EnumLineType"""

        timer2 = TicToc()
        timer2.tic()

        # Check enum types allowed
        if EnumLineType == LineType.PLUS:
            pass
        elif EnumLineType == LineType.STAR:
            pass
        else:
            print(f"{EnumLineType} is not allowed for this method")

        # Look for the required lineType
        mask = self.getLineTypes == EnumLineType
        if not np.any(mask == True):
            return
        maskPointerStart = np.where(mask)[0]
        matchString = self.data[mask].astype('U8')

        # Sort into reverse order
        sortIndices = np.argsort(maskPointerStart)[::-1]
        matchString = matchString[sortIndices]
        maskPointerStart = maskPointerStart[sortIndices]

        # Get the data and allow for the lines to be longer
        dataArray = self.data
        USize = int(dataArray.dtype.str.replace("<U", ""))

        for tp, blah in enumerate(maskPointerStart):
            tempMatchString = matchString[tp]
            IS = maskPointerStart[tp]
            IE = IS-1

            newLine1 = dataArray[IE]+dataArray[IS]
            newLine2 = newLine1.replace(tempMatchString, '')

            # Adjust the size of the array if necessary
            if len(newLine2) > USize:
                USize = len(newLine2)
                tempString = f"<U{USize}"
                print(f"\tResize Arrary: {tempString}")
                dataArray = dataArray.astype(tempString)

            dataArray[IE] = newLine2

        # Remove all the lines after data has been transferred
        dataArray = np.delete(dataArray, maskPointerStart)

        # Put the data back to self.
        self.data = dataArray

        # reset the lineTypes
        del self.getLineTypes
        self.getLineTypes

        timer2.toc(f"CombineLines: {EnumLineType.value}={len(matchString)}:")
        return self.data

    def __repr__(self):
        returnString = f"{self.data.size}"
        return returnString

    def read(self, fileName) -> Self:
        """Read in the raw data"""

        # print(os.getcwd())

        with open(fileName) as fileHandle:
            Lines = fileHandle.readlines()
        self.data = np.array(Lines)

        # Remove new line charcter from strings
        self.data = np.core.defchararray.replace(
            self.data, "\n", '', count=None)

        return self

    def display(self) -> None:
        print(self.data)

    @property
    def numberOfLines(self) -> int:
        """Get the number of lines in the file"""
        return len(self.data)

    def CountEnumType(self, enumType) -> int:
        return np.count_nonzero(self.getLineTypes == enumType)

    @property
    def getLineTypes(self) -> list:
        """Make a list of the LineTypes"""

        # Check if variable has already been calculated
        if hasattr(self, 'lineTypeList'):
            return self.lineTypeList
        print("\tCalculate: lineTypeList")

        # define the list
        self.lineTypeList = np.empty(self.numberOfLines, dtype=LineType)

        # fill the list
        for i, line in np.ndenumerate(self.data):
            self.lineTypeList[i] = self.getLineType(line)

        return self.lineTypeList

    @getLineTypes.deleter
    def getLineTypes(self) -> None:
        print("\tDelete: lineTypeList")
        del self.lineTypeList

    def getLineType(self, line) -> LineType:
        """get the line Type"""
        for tempLineType in LineType:
            if line.startswith(tempLineType.value):
                return tempLineType

        print("Unknown line")
        print(line)
        return None

    def deleteEnumType(self, EnumLineType):

        timer = TicToc()
        timer.tic()

        mask = self.getLineTypes == EnumLineType
        count0 = np.count_nonzero(mask)
        if not np.any(mask == True):
            return

        mask = np.invert(mask)

        count1 = self.numberOfLines
        self.data = self.data[mask]
        count2 = self.numberOfLines

        # reset the lineTypes
        del self.getLineTypes
        self.getLineTypes

        timer.toc(
            f"Delete: {EnumLineType.value}={count0} {count1} to {count2}:")


def debug():
    print("main: start")

    # fileNameIn="nastran_input.nas"
    fileNameIn = "../testCode.short.nas"
    # print(os.getcwd())

    nastranData = RawData(fileNameIn)


if __name__ == "__main__":
    debug()
