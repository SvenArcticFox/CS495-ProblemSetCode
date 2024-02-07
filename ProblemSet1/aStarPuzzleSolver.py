import sys
import pickle
import numpy as np


def main(argv):
    puzzleDict = None
    with open('puzzleDictionary.pkl', 'rb') as f:
        puzzleDict = pickle.load(f)

    print("Puzzle Dictionary successfully loaded.")

    puzzleMatrix = puzzleDict.get("puzzleMatrix")
    targetMatrix = puzzleDict.get("targetMatrix")
    h = puzzleDict.get("h")
    g = puzzleDict.get("g")
    zero_xIndex = puzzleDict.get("zero_xIndex")
    zero_yIndex = puzzleDict.get("zero_yIndex")

    print("Values successfully assigned from dictionary!")

    print(targetMatrix)
    print(puzzleMatrix)
    def manhattanDist(puzzleNum):
        targetX , targetY = np.where(targetMatrix == puzzleNum)
        puzzleX, puzzleY = np.where(puzzleMatrix == puzzleNum)

        xDist = abs(targetX - puzzleX)
        yDist = abs(targetY - puzzleY)

        return xDist + yDist

    print(manhattanDist(1))
    print(h)

if __name__ == "__main__":
    main(sys.argv)