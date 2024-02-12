import sys
import pickle
import numpy as np
from queue import PriorityQueue

class Board:
    def __int__(self):
        boardMatrix = np.zeros((4,4), dtype=int)
        manhattan = 0
        hamming = 0
        g = 0
        fscore = 0
        zero_yIndex = 0
        zero_xIndex = 0
        moves = ""



def main(argv):
    with open('puzzleDictionary.pkl', 'rb') as f:
        puzzleDict = pickle.load(f)

    print("Puzzle Dictionary successfully loaded.")

    rootBoard = Board()
    rootBoard.boardMatrix = puzzleDict.get("puzzleMatrix")
    targetMatrix = puzzleDict.get("targetMatrix")
    rootBoard.hamming = puzzleDict.get("hamming")
    rootBoard.g = puzzleDict.get("g")
    rootBoard.zero_xIndex = puzzleDict.get("zero_xIndex")
    rootBoard.zero_yIndex = puzzleDict.get("zero_yIndex")

    print("Values successfully assigned from dictionary!")

    print(targetMatrix)
    print(rootBoard.boardMatrix)

    def manhattanDist(puzzleNum, board):
        targetX , targetY = np.where(targetMatrix == puzzleNum)
        puzzleX, puzzleY = np.where(board.boardMatrix == puzzleNum)

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

    def moveLeft(zero_xIndex, zero_yIndex, g, puzzleMatrix):
        if (zero_xIndex == 0):
            return False
        neighbor = np.array(puzzleMatrix, copy=True)
        temp = neighbor[zero_xIndex - 1, zero_yIndex]
        neighbor[zero_xIndex - 1, zero_yIndex] = neighbor[zero_xIndex, zero_yIndex]
        zero_xIndex -= 1
        neighbor[zero_xIndex + 1, zero_yIndex] = temp
        g += 1
        return zero_xIndex, zero_yIndex, g, neighbor

    def moveRight(zero_xIndex, zero_yIndex, g, puzzleMatrix):
        if (zero_xIndex == 3):
            return False
        neighbor = np.array(puzzleMatrix, copy=True)
        temp = puzzleMatrix[zero_xIndex + 1, zero_yIndex]
        puzzleMatrix[zero_xIndex + 1, zero_yIndex] = puzzleMatrix[zero_xIndex, zero_yIndex]
        zero_xIndex += 1
        puzzleMatrix[zero_xIndex - 1, zero_yIndex] = temp
        g += 1
        return zero_xIndex, zero_yIndex, g

    def moveUp(zero_xIndex, zero_yIndex, g, puzzleMatrix):
        if (zero_yIndex == 0):
            return False
        temp = puzzleMatrix[zero_xIndex, zero_yIndex + 1]
        puzzleMatrix[zero_xIndex, zero_yIndex + 1] = puzzleMatrix[zero_xIndex, zero_yIndex]
        zero_yIndex += 1
        puzzleMatrix[zero_xIndex, zero_yIndex - 1] = temp
        g += 1
        return zero_xIndex, zero_yIndex, g

    def moveDown(zero_xIndex, zero_yIndex, g, puzzleMatrix):
        if (zero_yIndex == 0):
            return False
        temp = puzzleMatrix[zero_xIndex, zero_yIndex - 1]
        puzzleMatrix[zero_xIndex, zero_yIndex - 1] = puzzleMatrix[zero_xIndex, zero_yIndex]
        zero_yIndex -= 1
        puzzleMatrix[zero_xIndex, zero_yIndex + 1] = temp
        g += 1
        return zero_xIndex, zero_yIndex, g

    def calcAllManhattanDist(manhattanList, board):
        for i in range(16):
            manhattanList[i] = manhattanDist(i, board)

        return manhattanList

    manhattanList = np.zeros(16, dtype=int)
    calcAllManhattanDist(manhattanList, rootBoard)

    print(manhattanList)
    print(rootBoard.hamming)

if __name__ == "__main__":
    main(sys.argv)