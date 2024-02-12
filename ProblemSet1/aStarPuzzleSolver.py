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
def manhattanDist(puzzleNum, board, targetMatrix):
    targetX , targetY = np.where(targetMatrix == puzzleNum)
    puzzleX, puzzleY = np.where(board.boardMatrix == puzzleNum)

    xDist = abs(targetX - puzzleX)
    yDist = abs(targetY - puzzleY)

    return xDist + yDist

def calculateHammingDist(board, targetMatrix):
    hamming = 0
    for i in range(4):
        for j in range(4):
            if targetMatrix[i, j] != board.boardMatrix[i, j]:
                hamming += 1

    return hamming

def checkLeft(board):
    return board.zero_xIndex == 0

def checkRight(board):
    return board.zero_xIndex == 3

def checkUp(board):
    return board.zero_yIndex == 0

def checkDown(board):
    return board.zero_yIndex == 3

def moveLeft(board, targetMatrix):
    if (board.zero_xIndex == 0):
        return False

    neighbor = Board()
    neighbor.boardMatrix = np.array(board.puzzleMatrix, copy=True)
    neighbor.manhattan = board.manhattan
    neighbor.hamming = board.hamming
    neighbor.g = board.g
    neighbor.fscore = board.fscore
    neighbor.zero_yIndex = board.zero_yIndex
    neighbor.zero_xIndex = board.zero_xIndex
    neighbor.moves = neighbor.moves


    temp = neighbor.boardMatrix[neighbor.zero_xIndex - 1, neighbor.zero_yIndex]
    neighbor.boardMatrix[neighbor.zero_xIndex - 1, neighbor.zero_yIndex] \
        = neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex]
    neighbor.zero_xIndex -= 1
    neighbor.boardMatrix[neighbor.zero_xIndex + 1, neighbor.zero_yIndex] = temp
    neighbor.g += 1

    neighbor.moves += "L, "

    neighbor.hamming = calculateHammingDist(neighbor, targetMatrix)
    neighbor.manhattan = calcTotalManhattanDist(neighbor, targetMatrix)
    neighbor.fscore = neighbor.g + neighbor.manhattan

    return neighbor

def moveRight(board, targetMatrix):
    if (board.zero_xIndex == 3):
        return False

    neighbor = Board()
    neighbor.boardMatrix = np.array(board.puzzleMatrix, copy=True)
    neighbor.manhattan = board.manhattan
    neighbor.hamming = board.hamming
    neighbor.g = board.g
    neighbor.fscore = board.fscore
    neighbor.zero_yIndex = board.zero_yIndex
    neighbor.zero_xIndex = board.zero_xIndex
    neighbor.moves = neighbor.moves

    temp = neighbor.boardMatrix[neighbor.zero_xIndex + 1, neighbor.zero_yIndex]
    neighbor.boardMatrix[neighbor.zero_xIndex + 1, neighbor.zero_yIndex] \
        = neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex]
    neighbor.zero_xIndex += 1
    neighbor.boardMatrix[neighbor.zero_xIndex - 1, neighbor.zero_yIndex] = temp
    neighbor.g += 1

    neighbor.moves += "R, "

    neighbor.hamming = calculateHammingDist(neighbor, targetMatrix)
    neighbor.manhattan = calcTotalManhattanDist(neighbor, targetMatrix)
    neighbor.fscore = neighbor.g + neighbor.manhattan


    return neighbor

def moveUp(board, targetMatrix):
    if (board.zero_xIndex == 0):
        return False

    neighbor = Board()
    neighbor.boardMatrix = np.array(board.puzzleMatrix, copy=True)
    neighbor.manhattan = board.manhattan
    neighbor.hamming = board.hamming
    neighbor.g = board.g
    neighbor.fscore = board.fscore
    neighbor.zero_yIndex = board.zero_yIndex
    neighbor.zero_xIndex = board.zero_xIndex
    neighbor.moves = neighbor.moves

    temp = neighbor.boardMatrix[neighbor.zero_xIndex , neighbor.zero_yIndex + 1]
    neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex + 1] \
        = neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex]
    neighbor.zero_yIndex += 1
    neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex - 1] = temp
    neighbor.g += 1

    neighbor.moves += "U, "

    neighbor.hamming = calculateHammingDist(neighbor, targetMatrix)
    neighbor.manhattan = calcTotalManhattanDist(neighbor, targetMatrix)
    neighbor.fscore = neighbor.g + neighbor.manhattan

    return neighbor

def moveDown(board, targetMatrix):
    if (board.zero_xIndex == 0):
        return False

    neighbor = Board()
    neighbor.boardMatrix = np.array(board.puzzleMatrix, copy=True)
    neighbor.manhattan = board.manhattan
    neighbor.hamming = board.hamming
    neighbor.g = board.g
    neighbor.fscore = board.fscore
    neighbor.zero_yIndex = board.zero_yIndex
    neighbor.zero_xIndex = board.zero_xIndex
    neighbor.moves = neighbor.moves

    temp = neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex - 1]
    neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex - 1] \
        = neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex]
    neighbor.zero_yIndex -= 1
    neighbor.boardMatrix[neighbor.zero_xIndex, neighbor.zero_yIndex + 1] = temp
    neighbor.g += 1

    neighbor.moves += "U, "

    neighbor.hamming = calculateHammingDist(neighbor, targetMatrix)
    neighbor.manhattan = calcTotalManhattanDist(neighbor, targetMatrix)
    neighbor.fscore = neighbor.g + neighbor.manhattan

def calcTotalManhattanDist(board, targetMatrix):
    manhattan = 0
    for i in range(16):
        manhattan += manhattanDist(i, board, targetMatrix)

    return manhattan



def main(argv):
    with open('puzzleDictionary.pkl', 'rb') as f:
        puzzleDict = pickle.load(f)

    print("Puzzle Dictionary successfully loaded.")

    rootBoard = Board()
    rootBoard.boardMatrix = puzzleDict.get("puzzleMatrix")
    targetMatrix = puzzleDict.get("targetMatrix")
    rootBoard.hamming = puzzleDict.get("hamming")
    rootBoard.manhattan = puzzleDict.get("manhattan")
    rootBoard.g = puzzleDict.get("g")
    rootBoard.zero_xIndex = puzzleDict.get("zero_xIndex")
    rootBoard.zero_yIndex = puzzleDict.get("zero_yIndex")

    print("Values successfully assigned from dictionary!")

    print(targetMatrix)
    print(rootBoard.boardMatrix)


    print(rootBoard.manhattan)
    print(rootBoard.hamming)

if __name__ == "__main__":
    main(sys.argv)