import pytest
from load_testdata import load_json_testcases

def powerset(arr):
    if arr:
        first, *rest = arr #python3 just like car and cdr (in this case anyway..)
        rest_subsets = powerset(rest)
        # Include both subsets without 'first' and subsets with 'first'
        return [[first] + subset for subset in rest_subsets] + rest_subsets
    else:
        return [[]]
    


testdata = load_json_testcases(powerset.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_powerset(input_data, expected):
    assert powerset(*input_data) == expected
