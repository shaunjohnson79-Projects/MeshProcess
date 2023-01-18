import numpy as np

def ReadRawData(fileName) -> list:
    """Read in the raw data"""
    with open(fileName) as fileHandle:
        Lines = fileHandle.readlines()
    return Lines

def main():
    print("Hello World!")
    fileName="nastran_input.nas"
    Lines=ReadRawData(fileName)
    rr = np.array(Lines)
    print(rr)

if __name__ == "__main__":
    main()