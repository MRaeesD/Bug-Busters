import pytest
from load_testdata import load_json_testcases

def quicksort(arr):
    if not arr:
        return []

    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot])
    equal = [x for x in arr if x == pivot]  # Added to handle elements equal to the pivot
    greater = quicksort([x for x in arr[1:] if x > pivot])
    return lesser + equal + greater  # Changed to include 'equal' in the concatenation



testdata = load_json_testcases(quicksort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_quicksort(input_data, expected):
    assert quicksort(*input_data) == expected
