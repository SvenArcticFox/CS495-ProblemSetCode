# ProblemSet1

This problem set involves using the A* search algorithm, found here *https://coursera.cs.princeton.edu/algs4/assignments/8puzzle/specification.php*
and a divide and conquer method
found here *https://www.kopf.com.br/kaplof/how-to-solve-any-slide-puzzle-regardless-of-its-size/#google_vignette*
in order to solve a 4x4 sliding puzzle.

### Results
Running the two puzzles that require more than 100 moves take over 10 minutes to run on both algorithms. On simpler
puzzles, it seems that the divide and conquer algorithm takes a slightly longer time to solve a puzzle compared to the
A* algorithm. With puzzle 4, it took the A* algorithm about 5.5 seconds to run on average, and it took the divide
and conquer algorithm 6.5 seconds on average to run. Overall, the divide and conquer algorithm is slower than the 
A* algorithm.

### Requirements
- numpy

### Instructions to run
1. Open the generateMatrixDict.py file
   1. Optional: Change the puzzle matrix to a matrix that is in the *puzzles* directory
2. Run the generateMatrixDict.py file
3. Run the aStarPuzzleSolver.py file for A* solver algorithm
4. Run the divideAndConquer.py file for the divide and conquer solver algorithm