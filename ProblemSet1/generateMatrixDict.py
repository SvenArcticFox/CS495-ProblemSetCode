import sys
import numpy as np
import random
import pickle

def main(argv):
    targetMatrix = np.array([[1,2,3,4],
                               [5,6,7,8],
                               [9,10,11,12],
                               [13,14,15, 0]])


    charList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

    puzzleMatrix = np.zeros((4, 4), dtype=int)

    for i in range(4):
        for j in range(4):
            choice = random.randrange(0, len(charList))
            puzzleMatrix[i, j] = charList[choice]
            charList.remove(charList[choice])


    g = 0
    h = 0

    zero_xIndex = None
    zero_yIndex = None

    for i in range(4):
        for j in range(4):
            if targetMatrix[i,j] != puzzleMatrix[i,j]:
                h += 1
            if puzzleMatrix[i,j] == 0:
                zero_xIndex = i
                zero_yIndex = j

    puzzleDict = {
        "targetMatrix": targetMatrix,
        "puzzleMatrix": puzzleMatrix,
        "h": h,
        "g": g,
        "zero_xIndex": zero_xIndex,
        "zero_yIndex": zero_yIndex
    }

    print(puzzleDict)

    with open('puzzleDictionary.pkl', 'wb') as f:
        pickle.dump(puzzleDict, f)

    print("Dictionary successfully created and saved as puzzleDictionary.pkl!")


if __name__ == "__main__":
    main(sys.argv)