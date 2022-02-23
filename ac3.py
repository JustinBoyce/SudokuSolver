from typing import List, Tuple
import util


def ac3(domain: dict, binary_constraints: dict):
    """Implements the AC3 algorithm"""
    def run():
        # The queue contains a pair connecting every variable
        queue = util.construct_queue(binary_constraints)
        while queue:
            input_var, output_var = queue.pop()
            # If domain of input_var had to be revised, add all neighbors to input_var to queue
            if revise(input_var, output_var):
                if len(domain[input_var]) == 0:
                    return False
                for new_var in binary_constraints[input_var]:
                    queue.append((new_var, input_var))
        return True

    def revise(in_var: Tuple, out_var: Tuple):
        """Checks for arc consistency for one binary constraint pair."""
        # in_var is arc consistent with out_var iff for every value in
        # in_var's domain there exists some legal value of out_var.
        revised = False
        for val in domain[in_var]:
            # I should find a better statement to check for arc consistency
            if val in domain[out_var] and len(domain[out_var]) < 2:
                domain[in_var].remove(val)
                revised = True
        return revised
    return run()








