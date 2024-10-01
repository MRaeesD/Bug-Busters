import pytest
from load_testdata import load_json_testcases

def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1  # Fix: Set hi to len(arr) - 1 for zero-based index

    while lo <= hi:  # Fix: Change to while lo <= hi to handle all elements
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x < arr[mid]:  # Fix: Change to x < arr[mid] for correct binary search logic
            hi = mid - 1  # Fix: Exclude mid index by setting hi to mid - 1

        else:
            lo = mid + 1

    return -1


testdata = load_json_testcases(find_first_in_sorted.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_find_first_in_sorted(input_data, expected):
    assert find_first_in_sorted(*input_data) == expected
