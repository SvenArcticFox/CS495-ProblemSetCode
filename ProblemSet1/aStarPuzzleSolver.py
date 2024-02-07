import sys
import pickle
import numpy as np


def main(argv):
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

    def calculateHammingDist():
        hamming = 0
        for i in range(4):
            for j in range(4):
                if targetMatrix[i, j] != puzzleMatrix[i, j]:
                    hamming += 1

        return hamming

    print(manhattanDist(1))
    print(h)

if __name__ == "__main__":
    main(sys.argv)