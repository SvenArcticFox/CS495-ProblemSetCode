import sys
import pickle


def main(argv):
    puzzleDict = None
    with open('puzzleDictionary.pkl', 'rb') as f:
        puzzleDict = pickle.load(f)

    print("Puzzle Dictionary successfully loaded.")

    puzzleMatrix = puzzleDict.get("puzzleMatrix")
    targetMatrix = puzzleDict.get("targetMatrix")
    h = puzzleDict.get("h")
    g = puzzleDict.get("g")
    x_XIndex = puzzleDict.get("x_XIndex")
    x_YIndex = puzzleDict.get("x_YIndex")

    print("Values successfully assigned from dictionary!")

if __name__ == "__main__":
    main(sys.argv)