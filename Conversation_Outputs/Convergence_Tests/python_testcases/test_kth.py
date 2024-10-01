import pytest
from load_testdata import load_json_testcases

def kth(arr, k):
    # Base case handling
    if len(arr) == 1:  # BUG FIX: Handle single-element array
        return arr[0]  

    pivot = arr[0]
    below = [x for x in arr if x <= pivot]  # BUG FIX: Include elements equal to pivot in `below`
    above = [x for x in arr if x > pivot]

    num_less = len(below) - below.count(pivot)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k - num_lessoreq)  # BUG FIX: Adjust `k` for the `above` array
    else:
        return pivot


testdata = load_json_testcases(kth.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kth(input_data, expected):
    assert kth(*input_data) == expected
