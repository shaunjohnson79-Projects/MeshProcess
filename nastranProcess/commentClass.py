import numpy as np
from typing import Self
from dataclasses import dataclass
from pytictoc import TicToc

from .lineTypeClass import LineType
from .generalMethods import convertToFloat, convertToInt
from .generalMethods import divideEnumType


class CommentRaw():
    def __init__(self, rawData) -> None:
        # print("Pshell Init")
        self.rawData = np.ndarray

        tempLineType = LineType.COMMENT

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

    def convert(self, rawData, tempLineType=LineType.GRID) -> Self:
        """Convert the rawData"""
        # Start timer
        timer = TicToc()
        timer.tic()

        tempLines = rawData.data[rawData.getLineTypes == tempLineType]
        tempLines = np.array([s[1:] for s in tempLines])
        tempLines = np.char.replace(tempLines, '~', ';')
        tempLines = tempLines.tolist()

        commentList = []
        newLine = True
        tempLine = ''
        for comment in tempLines:
            if len(comment.strip()) == 0:
                newLine = True
                continue
            elif comment.startswith('$$'):
                newLine = True
                continue
            elif comment.startswith(' '):
                newLine = True
                continue
            elif comment.startswith('ANSA'):
                newLine = True
            else:
                newLine = False

            if newLine:
                # Add the tempLine to list
                commentList.append(tempLine)
                # print(tempLine)

                # Start a new tempLine
                tempLine = comment
            else:
                tempLine = tempLine+comment
        commentList.append(tempLine)

        self.rawData = np.asarray(commentList)

        timer.toc(
            f"Convert: {tempLineType.value}={rawData.CountEnumType(tempLineType)}: ")
        return self


class Comment():
    def __init__(self, rawData) -> None:
        # print("Pshell Init")
        self.array = np.ndarray
        self.value = int

        self.convert(rawData)

    def convert(self, rawData) -> Self:
        self.array = rawData
        self.value = rawData[0]
