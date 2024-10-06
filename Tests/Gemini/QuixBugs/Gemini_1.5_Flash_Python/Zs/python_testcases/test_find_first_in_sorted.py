import pytest
from load_testdata import load_json_testcases

def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    while lo < hi:  # Change made here
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1



testdata = load_json_testcases(find_first_in_sorted.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_find_first_in_sorted(input_data, expected):
    assert find_first_in_sorted(*input_data) == expected
