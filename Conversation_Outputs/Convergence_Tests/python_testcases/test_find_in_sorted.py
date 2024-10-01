import pytest
from load_testdata import load_json_testcases

def find_in_sorted(arr, x):
    # Bug 3: Missing Edge Case Handling for Empty Array
    if not arr:  # Return -1 if the array is empty
        return -1
    
    def binsearch(start, end):
        # Bug 1: Condition for Termination in binsearch
        if start >= end:  # Should be >= to handle cases where start might become greater than end
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            # Bug 2: Range for Recursive binsearch Calls
            return binsearch(mid + 1, end)  # Exclude mid in the next search range
        else:
            return mid

    return binsearch(0, len(arr))


testdata = load_json_testcases(find_in_sorted.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_find_in_sorted(input_data, expected):
    assert find_in_sorted(*input_data) == expected
