import pytest
from load_testdata import load_json_testcases

def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:  # BUGFIX: Changed '<' to '>' to find the smallest element greater than perm[i]
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = perm[j], perm[i]
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
                    return next_perm
    # BUGFIX: Handle the case where perm is already the last permutation
    return sorted(perm)  

# Example usage
print(next_permutation([3, 2, 4, 1]))  # Expected output: [3, 4, 1, 2]


testdata = load_json_testcases(next_permutation.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_next_permutation(input_data, expected):
    assert next_permutation(*input_data) == expected
