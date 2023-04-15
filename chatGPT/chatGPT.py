import numpy as np


def combineLines(dataArray, matchLines):

    for matchValue in matchLines:
        # print(matchValue)

        IS = np.flatnonzero(np.char.startswith(dataArray, matchValue))
        IE = np.flatnonzero(np.char.endswith(dataArray, matchValue))

        # IS = np.where(np.char.startswith(dataArray, matchValue))[0]
        # IE = np.where(np.char.endswith(dataArray, matchValue))[0]

        newLine1 = combined_lines = np.concatenate(
            (dataArray[IE], dataArray[IS]))
        newLine2 = ''.join(newLine1).replace(matchValue, '')
        # print(newLine2)

        dataArray[IE] = newLine2
        dataArray = np.delete(dataArray, IS)
        # print(len(dataArray))
    return dataArray


def main():
    dataArray = np.array(
        ['apples a1', 'a1 foobar', 'cowboy a2', 'a2 asdasd', 'a3 asdasd'])

    dataArray = dataArray.astype('U512')
    matchLines = np.array(['a1', 'a2', 'a3'])
    dataArray2 = combineLines(dataArray, matchLines)

    print(dataArray2)


if __name__ == "__main__":
    main()
