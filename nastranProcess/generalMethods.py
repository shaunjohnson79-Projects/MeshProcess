import numpy as np
import warnings


def divideStringArrayFixedWidth(tempLines, width) -> np.ndarray:

    # Define the character String
    tempDtype = f"U{width}"

    tempLines = np.array([s[8:] for s in tempLines])

    # Calculate the array size for a given delimation width
    arraySize = calculateArraySizeForString(tempLines, width)
    print(f"\tWidth:{width} Shape:{arraySize}")

    tempLines = np.array([string[i:i+width]
                         for string in tempLines for i in range(0, len(string), width)], dtype=tempDtype)
    tempLines = np.reshape(tempLines, arraySize)

    return tempLines


def divideEnumType(rawData, EnumType) -> np.ndarray:

    # Get the grid lines
    tempLines = rawData.data[rawData.getLineTypes == EnumType]

    # Calculate if to do a long or short read
    if np.any(np.char.find(tempLines, '*') >= 0):
        width = 16
    else:
        width = 8

    # Divide the lines by fixed width
    tempLines = divideStringArrayFixedWidth(tempLines, width)

    return tempLines


def calculateArraySizeForString(tempLines, width) -> list:
    """Calculate the array size for a given delimation width"""

    # print(tempLines)
    # print(np.shape(tempLines))
    NOC = int(np.dtype(tempLines.dtype).itemsize/4)
    # print(NOC)

    if (NOC % width) == 0:
        pass
    else:
        print(f"problems")
    arraySize = [np.size(tempLines), int(NOC/width)]
    return arraySize


def convertToFloat(tempValue) -> np.ndarray:
    tempValue = np.char.strip(tempValue)

    tempValue = np.core.defchararray.replace(tempValue, '-', 'e-')
    tempValue = np.core.defchararray.replace(tempValue, '+', 'e+')
    tempValue = np.core.defchararray.replace(tempValue, 'Ee', 'e')
    tempValue = np.core.defchararray.replace(tempValue, 'ee', 'e')

    mask = np.char.startswith(tempValue, 'e')
    tempValue[mask] = np.char.lstrip(tempValue[mask], 'e')

    # Replace empty cells with nan
    tempValue = np.where(tempValue == '', np.nan, tempValue)

    # Convert the data
    tempValue = tempValue.astype(float)

    return tempValue


def convertToInt(tempValue) -> np.ndarray:

    tempValue = np.char.strip(tempValue)

    tempValue = np.core.defchararray.replace(tempValue, '.', '')

    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
        # Replace empty cells with 0
        tempValue = np.where(tempValue == '', 0, tempValue)

    # Convert the data
    tempValue = tempValue.astype(int)

    return tempValue


def getEnum(name, EnumClass):
    if name in EnumClass.__members__:
        member = EnumClass[name]
        return member
    else:
        member = None
