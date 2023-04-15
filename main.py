import os
from nastranProcess.nastran import Nastran


def main():

    fileNameList = []

    # fileNameList.append("nastran_input.nas")
    # fileNameList.append("testCode.long.nas")
    fileNameList.append("testCode.short.nas")
    # fileNameList.append("testCode.shortXML.nas")
    print(os.getcwd())

    for fileName in fileNameList:
        nastranData = Nastran()
        nastranData.readfromFile(fileName)

    # print(nastranData)

    # print(nastranData.__dict__)
if __name__ == "__main__":
    main()
