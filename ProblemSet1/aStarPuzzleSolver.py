import sys
import pickle
import numpy as np
from queue import PriorityQueue
from datetime import datetime

class Board:
    def __int__(self):
        self.moves = ""
        self.boardMatrix = np.zeros((4,4), dtype=int)
        self.manhattan = 0
        self.hamming = 0
        self.g = 0
        self.fscore = 0
        self.zero_yIndex = 0
        self.zero_xIndex = 0

    def __lt__(self, other):
        return self.fscore < other.fscore



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
    return not board.zero_xIndex == 0

def checkRight(board):
    return not board.zero_xIndex == 3

def checkUp(board):
    return not board.zero_yIndex == 0

def checkDown(board):
    return not board.zero_yIndex == 3

def moveLeft(board, targetMatrix):
    if (board.zero_xIndex == 0):
        return False

    neighbor = Board()
    neighbor.boardMatrix = np.array(board.boardMatrix, copy=True)
    neighbor.manhattan = board.manhattan
    neighbor.hamming = board.hamming
    neighbor.g = board.g
    neighbor.fscore = board.fscore
    neighbor.zero_yIndex = board.zero_yIndex
    neighbor.zero_xIndex = board.zero_xIndex
    neighbor.moves = board.moves


    temp = neighbor.boardMatrix[ neighbor.zero_yIndex, neighbor.zero_xIndex - 1]
    neighbor.boardMatrix[neighbor.zero_yIndex, neighbor.zero_xIndex - 1] \
        = neighbor.boardMatrix[ neighbor.zero_yIndex, neighbor.zero_xIndex]
    neighbor.zero_xIndex -= 1
    neighbor.boardMatrix[neighbor.zero_yIndex, neighbor.zero_xIndex + 1] = temp
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
    neighbor.boardMatrix = np.array(board.boardMatrix, copy=True)
    neighbor.manhattan = board.manhattan
    neighbor.hamming = board.hamming
    neighbor.g = board.g
    neighbor.fscore = board.fscore
    neighbor.zero_yIndex = board.zero_yIndex
    neighbor.zero_xIndex = board.zero_xIndex
    neighbor.moves = board.moves

    temp = neighbor.boardMatrix[neighbor.zero_yIndex, neighbor.zero_xIndex + 1]
    neighbor.boardMatrix[neighbor.zero_yIndex, neighbor.zero_xIndex + 1] \
        = neighbor.boardMatrix[neighbor.zero_yIndex, neighbor.zero_xIndex]
    neighbor.zero_xIndex += 1
    neighbor.boardMatrix[neighbor.zero_yIndex, neighbor.zero_xIndex - 1] = temp
    neighbor.g += 1

    neighbor.moves += "R, "

    neighbor.hamming = calculateHammingDist(neighbor, targetMatrix)
    neighbor.manhattan = calcTotalManhattanDist(neighbor, targetMatrix)
    neighbor.fscore = neighbor.g + neighbor.manhattan


    return neighbor

def moveUp(board, targetMatrix):
    if (board.zero_yIndex == 0):
        return False

    neighbor = Board()
    neighbor.boardMatrix = np.array(board.boardMatrix, copy=True)
    neighbor.manhattan = board.manhattan
    neighbor.hamming = board.hamming
    neighbor.g = board.g
    neighbor.fscore = board.fscore
    neighbor.zero_yIndex = board.zero_yIndex
    neighbor.zero_xIndex = board.zero_xIndex
    neighbor.moves = board.moves

    temp = neighbor.boardMatrix[neighbor.zero_yIndex - 1, neighbor.zero_xIndex]
    neighbor.boardMatrix[neighbor.zero_yIndex - 1, neighbor.zero_xIndex] \
        = neighbor.boardMatrix[neighbor.zero_yIndex, neighbor.zero_xIndex]
    neighbor.zero_yIndex -= 1
    neighbor.boardMatrix[neighbor.zero_yIndex + 1, neighbor.zero_xIndex] = temp
    neighbor.g += 1

    neighbor.moves += "U, "

    neighbor.hamming = calculateHammingDist(neighbor, targetMatrix)
    neighbor.manhattan = calcTotalManhattanDist(neighbor, targetMatrix)
    neighbor.fscore = neighbor.g + neighbor.manhattan

    return neighbor

def moveDown(board, targetMatrix):
    if (board.zero_yIndex == 3):
        return False

    neighbor = Board()
    neighbor.boardMatrix = np.array(board.boardMatrix, copy=True)
    neighbor.manhattan = board.manhattan
    neighbor.hamming = board.hamming
    neighbor.g = board.g
    neighbor.fscore = board.fscore
    neighbor.zero_yIndex = board.zero_yIndex
    neighbor.zero_xIndex = board.zero_xIndex
    neighbor.moves = board.moves

    temp = neighbor.boardMatrix[neighbor.zero_yIndex + 1, neighbor.zero_xIndex]
    neighbor.boardMatrix[neighbor.zero_yIndex + 1, neighbor.zero_xIndex] \
        = neighbor.boardMatrix[neighbor.zero_yIndex, neighbor.zero_xIndex]
    neighbor.zero_yIndex += 1
    neighbor.boardMatrix[neighbor.zero_yIndex - 1, neighbor.zero_xIndex] = temp
    neighbor.g += 1

    neighbor.moves += "D, "

    neighbor.hamming = calculateHammingDist(neighbor, targetMatrix)
    neighbor.manhattan = calcTotalManhattanDist(neighbor, targetMatrix)
    neighbor.fscore = neighbor.g + neighbor.manhattan

    return neighbor

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
    rootBoard.moves = ""

    print("Values successfully assigned from dictionary!")

    print("Target:\n", targetMatrix)
    print("Board:\n", rootBoard.boardMatrix)


    print(rootBoard.manhattan)
    print(rootBoard.hamming)

    visited = []
    visited.append(rootBoard.boardMatrix.tolist())



    rootBoard.fscore = rootBoard.manhattan + rootBoard.g
    pq = PriorityQueue()
    pq.put((rootBoard.fscore, rootBoard))


    global targetFound
    targetFound = False

    global board

    start = datetime.now().timestamp()

    while not pq.empty() and not targetFound:
        fscore,board = pq.get() # add a tiebreaker to prevent queue from comparing arrays

        print("Board:", "\n", board.boardMatrix)
        print("F-Score:", board.fscore, "\t", "G:", board.g, "\t", "Manhattan:", board.manhattan, "\t", "Hamming:",
              board.hamming, "\t", "Zero X Index:", board.zero_xIndex, "\t", "Zero Y Index:", board.zero_yIndex ,"\n",
              "Moves Made:", board.moves, "\n")

        if np.array_equal(board.boardMatrix, targetMatrix):
            targetFound = True
            continue

        if checkLeft(board):
            neighborLeft = moveLeft(board, targetMatrix)
            if neighborLeft.boardMatrix.tolist() not in visited:
                visited.append(neighborLeft.boardMatrix.tolist())
                pq.put((neighborLeft.fscore, neighborLeft))

        if checkRight(board):
            neighborRight = moveRight(board, targetMatrix)
            if neighborRight.boardMatrix.tolist() not in visited:
                visited.append(neighborRight.boardMatrix.tolist())
                pq.put((neighborRight.fscore, neighborRight))

        if checkUp(board):
            neighborUp = moveUp(board, targetMatrix)
            if neighborUp.boardMatrix.tolist() not in visited:
                visited.append(neighborUp.boardMatrix.tolist())
                pq.put((neighborUp.fscore, neighborUp))

        if checkDown(board):
            neighborDown = moveDown(board, targetMatrix)
            if neighborDown.boardMatrix.tolist() not in visited:
                visited.append(neighborDown.boardMatrix.tolist())
                pq.put((neighborDown.fscore, neighborDown))

    end = datetime.now().timestamp()
    timeRun = end - start

    print("************************** FINAL BOARD **************************")
    print("Board:", "\n", board.boardMatrix)
    print("F-Score:", board.fscore, "\t", "G:", board.g, "\t", "Manhattan:", board.manhattan, "\t", "Hamming:",
          board.hamming, "\t", "Zero X Index:", board.zero_xIndex, "\t", "Zero Y Index:", board.zero_yIndex, "\n",
          "Moves Made:", board.moves, "\n")
    print("Time run:", timeRun, "seconds!")




if __name__ == "__main__":
    main(sys.argv)