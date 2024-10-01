import pytest
from load_testdata import load_json_testcases

def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Collect lengths of subsequences that can be extended by val
        # Fix: Check if key 'j' exists in 'ends' before accessing 
        prefix_lengths = [j for j in range(1, longest + 1) if j in ends and arr[ends[j]] < val] 

        length = max(prefix_lengths) if prefix_lengths else 0

        # Fix: Ensure the subsequence is increasing and handle potential KeyError
        if length == longest or (length + 1 not in ends or val < arr[ends[length + 1]]):  
            ends[length + 1] = i
            # Fix: Update 'longest' correctly
            longest = max(longest, length + 1) 

    return longest


testdata = load_json_testcases(lis.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lis(input_data, expected):
    assert lis(*input_data) == expected
