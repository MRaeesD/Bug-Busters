import pytest
from load_testdata import load_json_testcases

def powerset(arr):
        if arr:
            first, *rest = arr
            rest_subsets = powerset(rest)
            # Include subsets with and without 'first'
            return rest_subsets + [[first] + subset for subset in rest_subsets]  # Fix: Add 'rest_subsets +' to include subsets without 'first'
        else:
            return [[]]



testdata = load_json_testcases(powerset.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_powerset(input_data, expected):
    assert powerset(*input_data) == expected
