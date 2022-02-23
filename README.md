# SudokuSolver
Solves 9x9 Sudoku problems as a CSP using an a backtracking algorithm with forward checking. Also has an option to add in the use of the AC3 algorithm to improve performance. 

backtracking.py contains just the backtracking algorithm, forward_checking.py is similar to backtracking.py but it adds in forward checking. ac3.py implements the AC3 (arc consistency) algorithm. These algorithms should work for any CSP, but have not been tested. test_cases.py contains six sudoku puzzles in the form of a 9x9 2d list.
