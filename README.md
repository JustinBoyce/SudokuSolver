# SudokuSolver
Solves 9x9 Sudoku problems as a CSP using an a backtracking algorithm with forward checking. Also has an option to add in the use of the AC3 algorithm to improve performance. 

backtracking.py contains just the backtracking algorithm, forward_checking.py is similar to backtracking.py but it adds in forward checking. ac3.py implements the AC3 (arc consistency) algorithm. These algorithms should work for any CSP, but have not been tested. test_cases.py contains six sudoku puzzles in the form of a 9x9 2d list.

## Test Instructions
To run test cases you must have python 3 installed. Download the files onto your local machine, then run the following command:

  `python sudoku_solver.py`
  
This will run 6 test sudoku puzzles and print out their results to the console.
