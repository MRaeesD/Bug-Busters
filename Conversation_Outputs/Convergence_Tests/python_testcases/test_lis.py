import pytest
from load_testdata import load_json_testcases

def lis(arr):
    ends = {}
    longest = 0

    # Initialize ends[1] here for subsequences of length 1
    if arr:
        ends[1] = 0

    for i, val in enumerate(arr):
        # Initialize a temporary list for prefix lengths
        prefix_lengths = []
        
        # Iterate through ends to find all valid lengths
        for j in range(1, longest + 1):
            if j in ends and arr[ends[j]] < val:  # Ensure j is in ends
                prefix_lengths.append(j)

        length = max(prefix_lengths) if prefix_lengths else 0

        # Handling potential KeyError by checking if length + 1 is in ends
        if length == longest or (length + 1 not in ends or val < arr[ends[length + 1]]):
            ends[length + 1] = i
            longest = length + 1

    return longest

# Test cases
test_cases = [
    [4, 1, 5, 3, 7, 6, 2],  # Expected output: 3
    [1, 2, 3, 4, 5],         # Expected output: 5
    [5, 4, 3, 2, 1],         # Expected output: 1
    [10, 9, 2, 5, 3, 7, 101, 18] # Expected output: 4
]

for case in test_cases:
    print(f"Input: {case}, LIS Length: {lis(case)}")


testdata = load_json_testcases(lis.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lis(input_data, expected):
    assert lis(*input_data) == expected
