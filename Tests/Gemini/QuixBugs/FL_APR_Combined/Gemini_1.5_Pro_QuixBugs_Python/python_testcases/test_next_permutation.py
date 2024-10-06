import pytest
from load_testdata import load_json_testcases

def next_permutation(perm):
                for i in range(len(perm) - 2, -1, -1):
                    if perm[i] < perm[i + 1]:
                        for j in range(len(perm) - 1, i, -1):
                            # Fix: Changed the comparison operator to '>'
                            if perm[j] > perm[i]: 
                                next_perm = list(perm)
                                next_perm[i], next_perm[j] = perm[j], perm[i]
                                next_perm[i + 1:] = reversed(next_perm[i + 1:])
                                return next_perm


testdata = load_json_testcases(next_permutation.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_next_permutation(input_data, expected):
    assert next_permutation(*input_data) == expected
