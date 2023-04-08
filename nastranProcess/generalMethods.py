import numpy as np

def divideStringArrayFixedWidth(tempLines,width) -> np.ndarray:
    
    #Calculate the array size for a given delimation width
    arraySize=calculateArraySizeForString(tempLines,width)
    
    tempLines=np.array([string[i:i+width] for string in tempLines for i in range(0, len(string), width)], dtype='U8')
    tempLines=np.reshape(tempLines,arraySize)
    
    return tempLines

def calculateArraySizeForString(tempLines,width) -> list:
    """Calculate the array size for a given delimation width"""
    NOC=int(np.dtype(tempLines.dtype).itemsize/4)
    if (NOC % width) == 0:
        pass
    else:
        print(f"problems")
    arraySize=[np.size(tempLines),int(NOC/width)]
    return arraySize   

def convertToFloat(tempValue) -> np.ndarray:
    
    tempValue = np.core.defchararray.replace(tempValue, '-', 'e-')
    tempValue = np.core.defchararray.replace(tempValue, '+', 'e+')
    remove_e = lambda x: x if x[0]!='e' else x[1:]
    remove_e = np.vectorize(remove_e)
    tempValue = remove_e(tempValue)
    
    return tempValue.astype(float) 