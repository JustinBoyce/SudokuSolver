from typing import List, Tuple

import util
from ac3 import ac3
from forward_checking import forward_checking
import test_cases


def main():
    # a means using forward_checking and b means using ac3
    # I did this, so it matches the homework prompt
    a: bool = True
    b: bool = False
    # Test and print all 6 example sudoku puzzles alternating between a and b algorithms
    util.print_sudoku(sudoku_solver(test_cases.initial_sud, a))
    util.print_sudoku(sudoku_solver(test_cases.initial_sud2, b))
    util.print_sudoku(sudoku_solver(test_cases.initial_sud3, a))
    util.print_sudoku(sudoku_solver(test_cases.initial_sud4, b))
    util.print_sudoku(sudoku_solver(test_cases.initial_sud5, a))
    util.print_sudoku(sudoku_solver(test_cases.initial_sud6, b))


def sudoku_solver(initial_s: List[List[int]], algo: bool = True):
    """Takes a list of lists sudoku input and outputs a solved version."""
    """
    We are going to solve sudoku as a CSP. Our variables will be the indices that can be changed. Our domain will start
    as the digits from 1 to 9. Our constraints will be that no variable can have the same value as another variable that 
    is within the same row, column, or ninth. Note that our variables are defined only at indices where the number is 
    not fixed. Thus we will treat the other indices as unary constraints which will be handled by our node_consistency
    function.
    """
    # a means using forward_checking and b means using ac3
    # I did this, so it matches the homework prompt
    a: bool = True
    b: bool = False

    # Tuple that represents the index of each spot that can be changed
    unassigned_variables: List[Tuple] = []
    # List of possible values for each variable
    domain: dict = {}
    # dict that takes a variable tuple and returns a list of variable tuples that are constrained with the given key
    binary_constraints: dict = {}
    # Initialize domain and range
    for i in range(len(initial_s)):
        for j in range(len(initial_s[i])):
            if initial_s[i][j] == 0:
                # Store a tuple that denotes the location of each variable in variable list
                unassigned_variables.append((i, j))
                # Initialize each variable to have a domain that we can update
                domain.update({(i, j): [1, 2, 3, 4, 5, 6, 7, 8, 9]})
    # Construct dict of constraints between variables
    for var in unassigned_variables:
        # Create a blank list for every variable tuple
        binary_constraints.update({var: []})
        # Populate the list with variables they are constrained with according to the rules of sudoku
        for otherVar in unassigned_variables:
            if var != otherVar and util.is_constrained(var, otherVar):
                binary_constraints[var].append(otherVar)

    # This will look at all indices in our sudoku board that cannot be changed and
    # remove it from the domain of our variables. This represents taking care of our unary constraints.
    node_consistency(initial_s, domain)

    # Use ac3 first if specified
    if algo == b:
        ac3_success = ac3(domain, binary_constraints)
        # Check if there is not a solution according to ac3
        if not ac3_success:
            return "No solution"

    # Use backtracking algorithm with forward checking
    assigned_variables = forward_checking(domain, binary_constraints, unassigned_variables)
    if assigned_variables is None:
        return "No Solution"
    # Assign variables according to algorithm
    for var in assigned_variables:
        initial_s[var[0]][var[1]] = assigned_variables[var]
    # Check if it worked
    if util.check_sudoku(initial_s):
        if algo == a:
            print("Successfully found solution using backtracking and forward-checking!")
        if algo == b:
            print("Successfully found solution using AC3!")

    return initial_s


def node_consistency(initial_s: List[List], domain: dict) -> dict:
    """Enforces all unary constraints by removing disallowed values from domain of each variable."""
    for var in domain:
        for index in util.constrained_indices(var):
            if initial_s[index[0]][index[1]] in domain[var]:
                domain[var].remove(initial_s[index[0]][index[1]])


if __name__ == '__main__':
    main()
