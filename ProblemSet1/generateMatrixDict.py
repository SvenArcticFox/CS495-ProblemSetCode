import sys
import numpy as np
import random
import pickle

def main(argv):
    targetMatrix = np.array([[1,2,3,4],
                               [5,6,7,8],
                               [9,10,11,12],
                               [13,14,15,'x']])


    charList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'x']

    puzzleMatrix = np.array([[None, None, None, None],
                            [None, None, None, None],
                            [None, None, None,None],
                            [None, None, None, None]])

    for i in range(4):
        for j in range(4):
            choice = random.randrange(0, len(charList))
            puzzleMatrix[i, j] = charList[choice]
            charList.remove(charList[choice])


    g = 0
    h = 0

    x_XIndex = None
    x_YIndex = None

    for i in range(4):
        for j in range(4):
            if targetMatrix[i,j] != puzzleMatrix[i,j]:
                h += 1
            if puzzleMatrix[i,j] == 'x':
                x_XIndex = i
                x_YIndex = j

    puzzleDict = {
        "targetMatrix": targetMatrix,
        "puzzleMatrix": puzzleMatrix,
        "h": h,
        "g": g,
        "x_xIndex": x_XIndex,
        "x_yIndex": x_YIndex
    }

    print(puzzleDict)

    with open('puzzleDictionary.pkl', 'wb') as f:
        pickle.dump(puzzleDict, f)

    print("Dictionary successfully created and saved as puzzleDictionary.pkl!")
if __name__ == "__main__":
    main(sys.argv)