import pytest
from load_testdata import load_json_testcases

def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start > end:  # Correct base case condition
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid - 1)  # Correct recursive call range
        elif x > arr[mid]:
            return binsearch(mid + 1, end)  # Correct recursive call range
        else:
            return mid

    return binsearch(0, len(arr) - 1)  # Correct initial call boundary


testdata = load_json_testcases(find_in_sorted.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_find_in_sorted(input_data, expected):
    assert find_in_sorted(*input_data) == expected
