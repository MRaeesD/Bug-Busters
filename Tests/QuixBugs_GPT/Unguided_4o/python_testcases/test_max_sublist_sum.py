import pytest
from load_testdata import load_json_testcases

def max_sublist_sum(arr):
    # Initialize variables to handle negative numbers correctly
    max_ending_here = 0
    max_so_far = float('-inf')
    
    for x in arr:
        # Add the current element to the maximum sum ending at this position
        max_ending_here = max_ending_here + x
        # If max_end_here is less than the current element, start a new subarray from here
        max_ending_here = max(x, max_ending_here)
        # Update max_so_far to hold the maximum of the two
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


testdata = load_json_testcases(max_sublist_sum.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_max_sublist_sum(input_data, expected):
    assert max_sublist_sum(*input_data) == expected
