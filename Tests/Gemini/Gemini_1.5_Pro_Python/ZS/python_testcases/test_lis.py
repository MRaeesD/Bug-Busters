import pytest
from load_testdata import load_json_testcases

def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or (length + 1 in ends and val < arr[ends[length + 1]]):  # Conditional update to longest
            ends[length + 1] = i
            if length + 1 > longest:  # Update longest only if a longer subsequence is found
                longest = length + 1

    return longest



testdata = load_json_testcases(lis.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lis(input_data, expected):
    assert lis(*input_data) == expected
