import pytest
from load_testdata import load_json_testcases

def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k - num_less - 1)  # Changed line to account for offset
    else:
        return pivot


testdata = load_json_testcases(kth.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kth(input_data, expected):
    assert kth(*input_data) == expected
