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

    def checkLeft(zero_xIndex):
        return zero_xIndex == 0

    def checkRight(zero_xIndex):
        return zero_xIndex == 3

    def checkUp(zero_yIndex):
        return zero_yIndex == 0

    def checkDown(zero_yIndex):
        return zero_yIndex == 3

    def moveLeft(zero_xIndex, zero_yIndex, g):
        if (zero_xIndex == 0):
            return False
        temp = puzzleMatrix[zero_xIndex - 1, zero_yIndex]
        puzzleMatrix[zero_xIndex - 1, zero_yIndex] = puzzleMatrix[zero_xIndex, zero_yIndex]
        zero_xIndex -= 1
        puzzleMatrix[zero_xIndex + 1, zero_yIndex] = temp
        g += 1
        return zero_xIndex, zero_yIndex, g

    def moveRight(zero_xIndex, zero_yIndex, g):
        if (zero_xIndex == 3):
            return False
        temp = puzzleMatrix[zero_xIndex + 1, zero_yIndex]
        puzzleMatrix[zero_xIndex + 1, zero_yIndex] = puzzleMatrix[zero_xIndex, zero_yIndex]
        zero_xIndex += 1
        puzzleMatrix[zero_xIndex - 1, zero_yIndex] = temp
        g += 1
        return zero_xIndex, zero_yIndex, g

    def moveUp(zero_xIndex, zero_yIndex, g):
        if (zero_yIndex == 0):
            return False
        temp = puzzleMatrix[zero_xIndex, zero_yIndex + 1]
        puzzleMatrix[zero_xIndex, zero_yIndex + 1] = puzzleMatrix[zero_xIndex, zero_yIndex]
        zero_yIndex += 1
        puzzleMatrix[zero_xIndex, zero_yIndex - 1] = temp
        g += 1
        return zero_xIndex, zero_yIndex, g

    def moveDown(zero_xIndex, zero_yIndex, g):
        if (zero_yIndex == 0):
            return False
        temp = puzzleMatrix[zero_xIndex, zero_yIndex - 1]
        puzzleMatrix[zero_xIndex, zero_yIndex - 1] = puzzleMatrix[zero_xIndex, zero_yIndex]
        zero_yIndex -= 1
        puzzleMatrix[zero_xIndex, zero_yIndex + 1] = temp
        g += 1
        return zero_xIndex, zero_yIndex, g

    def calcAllManhattanDist(manhattanList):
        for i in range(15):
            manhattanList[i] = manhattanDist(i)

        return manhattanList

    manhattanList = np.zeros(16, dtype=int)
    calcAllManhattanDist(manhattanList)

    print(manhattanList)
    print(h)

if __name__ == "__main__":
    main(sys.argv)