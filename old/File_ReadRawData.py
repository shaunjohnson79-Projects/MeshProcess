import numpy as np

def ReadRawData(fileName) -> np:
    """Read in the raw data"""
    with open(fileName) as fileHandle:
        Lines = fileHandle.readlines()
    rawData=np.array(Lines)
    
    # Remove new line charcter from strings
    rawData=np.core.defchararray.replace(rawData,"\n",'', count=None) 
    
    return rawData


def ReadRawDataV2(fileName) -> None:
    print("Hello World!")