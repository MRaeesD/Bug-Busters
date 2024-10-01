import pytest
from load_testdata import load_json_testcases

def max_sublist_sum(arr):
    if not arr:
        return 0  # Handle empty array case
    
    max_ending_here = arr[0]  # Initialize to the first element of the array
    max_so_far = arr[0]  # Initialize to the first element of the array

    for x in arr[1:]:  # Start from the second element
        max_ending_here = max(x, max_ending_here + x)  # Reset if max_ending_here becomes negative
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


testdata = load_json_testcases(max_sublist_sum.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_max_sublist_sum(input_data, expected):
    assert max_sublist_sum(*input_data) == expected
