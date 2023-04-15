import numpy as np
from typing import Self
from dataclasses import dataclass
from pytictoc import TicToc

from .lineTypeClass import LineType, AnsaComment
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
                if len(tempLine) != 0:
                    commentList.append(tempLine)
                    # print(tempLine)

                # Start a new tempLine
                tempLine = comment
            else:
                tempLine = tempLine+comment
        commentList.append(tempLine)

        self.data = np.asarray(commentList)
        # print(self.data)
        self.getCommentType

        timer.toc(
            f"Convert: {tempLineType.value}={rawData.CountEnumType(tempLineType)}: ")
        return self

    @property
    def getCommentType(self) -> list:
        """Make a list of the CommentType"""

        # Check if variable has already been calculated
        # if hasattr(self, 'commentTypeList'):
        #    return self.commentTypeList
        print("\tCalculate: commentTypeList")

        # define the list
        self.commentTypeList = np.empty(self.numberOfLines, dtype=AnsaComment)

        # fill the list
        for i, line in np.ndenumerate(self.data):
            self.commentTypeList[i] = self.getAnsaComment(line)

        return self.commentTypeList

    @getCommentType.deleter
    def CommentType(self) -> None:
        print("\tDelete: commentTypeList")
        del self.commentTypeList

    def getAnsaComment(self, line) -> AnsaComment:
        """get the AnsaComment"""
        for tempAnsaComment in AnsaComment:
            if line.startswith(tempAnsaComment.value):
                return tempAnsaComment

        print("Unknown line")
        print(line)
        return None

    @property
    def numberOfLines(self) -> int:
        """Get the number of lines in the file"""
        return len(self.data)


class Comment():
    def __init__(self, rawData) -> None:
        # print("Pshell Init")
        self.array = np.ndarray
        self.value = int

        self.convert(rawData)

    def convert(self, rawData) -> Self:
        self.array = rawData
        self.value = rawData[0]
