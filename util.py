from typing import Tuple, List


def is_constrained(var1: Tuple, var2: Tuple):
    """Returns true if var1 tuple is in the same row, column, or ninth as var2 tuple. Only works for 9x9 sudoku."""
    return (var1[0] // 3) == (var2[0] // 3) and (var1[1] // 3) == (var2[1] // 3) or \
           (var1[0] == var2[0]) or (var1[1] == var2[1])


def constrained_indices(var: Tuple):
    """Returns a list of all indices that within the same row, column, or ninth as var."""
    size_of_board: int = 9
    constrained_list: List[Tuple] = []
    # Add rows and columns
    for i in range(size_of_board):
        if (i, var[1]) != var:
            constrained_list.append((i, var[1]))
        if (var[0], i) != var:
            constrained_list.append((var[0], i))
    jth: int = 3 * (var[0] // 3)
    kth: int = 3 * (var[1] // 3)
    # Add indices in the common ninth
    for j in range(jth, jth + size_of_board // 3):
        for k in range(kth, kth + size_of_board // 3):
            if (j, k) != var and (j, k) not in constrained_list:
                constrained_list.append((j, k))

    return constrained_list


def check_sudoku(s: List[List[int]], size: int = 9):
    """Returns true if sudoku solution is valid"""
    # Not the most efficient but it works for our purposes
    for i in range(size):
        for j in range(size):
            for indices in constrained_indices((i, j)):
                if s[indices[0]][indices[1]] == s[i][j]:
                    return False
    return True


def construct_queue(binary_constraints: dict) -> List:
    """Constructs a queue (as a list) that contains every pair of variables as a tuple"""
    queue_of_arcs = []
    for in_variable in binary_constraints:
        for out_variable in binary_constraints[in_variable]:
            queue_of_arcs.append((in_variable, out_variable))
    return queue_of_arcs


def print_sudoku(s: List[List[int]]):
    """Prints a list of lists representation of a sudoku board with better formatting."""
    for line in s:
        print(line)
    print()

