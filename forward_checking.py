from typing import List, Tuple


def forward_checking(domain: dict, binary_constraints: dict, unassigned_variables: List[Tuple]) -> dict:
    """
    Takes a domain, binary constraints, unassigned variables and then returns the variables assigned in a dict.
    This should work with any CSP. Implements backtracking with forward-checking.
    """
    num_vars = len(unassigned_variables)
    assigned_variables: dict = {}

    def backtrack_w_forward_checking(assigned_vars: dict) -> dict:
        """Returns a dictionary representing variables and their correct values."""
        # If all vars have been assigned then we are done
        if len(assigned_vars) == num_vars:
            return assigned_vars
        # Take some unassigned var
        curr_var = unassigned_variables.pop()
        # Try every value in its domain
        for value in domain[curr_var]:
            assigned_vars.update({curr_var: value})
            # Make an inference/check forward
            valid_inference, inference_list = make_inference(curr_var, value)
            if valid_inference:
                # Recursive case: when value has been assigned and is allowed
                result = backtrack_w_forward_checking(assigned_vars)
                if result is not None:
                    return result
            assigned_vars.pop(curr_var)
            undo_inference(inference_list, value)
        # Re-add variable if assignment fails
        unassigned_variables.append(curr_var)
        # Return none if no valid state has been reached
        return None

    def make_inference(variable: Tuple, value: int):
        """
        Checks the variables that are constrained with input variable and removes value from their domain.
        Tracks an inference variable that can be used to undo these changes. Returns true if there every variable still
        has a valid value, false otherwise. Also returns a list of affected variables
        """
        variables_affected: List[Tuple] = []
        valid: bool = True
        for var in binary_constraints[variable]:
            if value in domain[var]:
                variables_affected.append(var)
                domain[var].remove(value)
                if len(domain[var]) == 0:
                    valid = False
        return valid, variables_affected

    def undo_inference(variables_affected: List[Tuple], value: int):
        """Uses variables_affected list to undo the changes made by make_inference"""
        for var in variables_affected:
            domain[var].append(value)

    return backtrack_w_forward_checking(assigned_variables)

