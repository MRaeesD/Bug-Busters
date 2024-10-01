import pytest
from load_testdata import load_json_testcases

def next_permutation(perm):
    # Step 1: Find the largest index i such that perm[i] < perm[i + 1]
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            # Step 2: Find the largest index j such that perm[j] > perm[i]
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:  # Fix: Corrected comparison to >
                    # Step 3: Swap elements at i and j
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = perm[j], perm[i]
                    # Step 4: Reverse the sublist from i+1 to the end
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
                    return next_perm
    # Edge Case: If no such i is found, return the smallest permutation (sorted in ascending order)
    return sorted(perm)  # Fix: Handle edge case and ensure a return value


testdata = load_json_testcases(next_permutation.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_next_permutation(input_data, expected):
    assert next_permutation(*input_data) == expected
