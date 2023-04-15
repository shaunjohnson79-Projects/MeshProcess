import os
from nastranProcess.nastran import Nastran


def main():
    print("main: start")
    fileNameIn = "nastran_input.nas"
    # fileNameIn = "testCode.long.nas"
    # fileNameIn = "testCode.short.nas"
    print(os.getcwd())

    nastranData = Nastran()
    nastranData.readfromFile(fileNameIn)

    # print(nastranData)

    # print("main: end")


    # print(nastranData.__dict__)
if __name__ == "__main__":
    main()
