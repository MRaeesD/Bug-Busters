import pytest
from load_testdata import load_json_testcases

def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        # Fix: Include both subsets that include 'first' and those that do not
        return rest_subsets + [[first] + subset for subset in rest_subsets]
    else:
        return [[]]


testdata = load_json_testcases(powerset.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_powerset(input_data, expected):
    assert powerset(*input_data) == expected
