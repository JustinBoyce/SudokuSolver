from typing import List, Tuple


def backtracking(domain: dict, binary_constraints: dict, unassigned_variables: List[Tuple]) -> dict:
    """
    Takes a domain, binary constraints, unassigned variables and then returns the variables assigned in a dict.
    This should work with any CSP. Implements only backtracking, no forward-checking.
    """
    num_vars = len(unassigned_variables)
    assigned_variables: dict = {}

    def backtrack(assigned_vars: dict) -> dict:
        # If all vars have been assigned then we are done
        if len(assigned_vars) == num_vars:
            return assigned_vars
        # Take some unassigned var
        curr_var = unassigned_variables.pop()
        # Try every value in its domain
        for value in domain[curr_var]:
            assigned_vars.update({curr_var: value})
            # Make an inference/check forward
            if check_constraint(curr_var, value):
                # Recursive case: when value has been assigned and is allowed
                result = backtrack(assigned_vars)
                if result is not None:
                    return result
                else:
                    assigned_vars.pop(curr_var)
            else:
                assigned_vars.pop(curr_var)
        # Re-add variable if assignment fails
        unassigned_variables.append(curr_var)
        # Return none if no valid state has been reached
        return None

    def check_constraint(variable: Tuple, value: int) -> bool:
        """Checks if value for variable is legal within the constraints"""
        for con_var in binary_constraints[variable]:
            if con_var in assigned_variables and assigned_variables[con_var] == value:
                return False
        return True

    return backtrack(assigned_variables)


