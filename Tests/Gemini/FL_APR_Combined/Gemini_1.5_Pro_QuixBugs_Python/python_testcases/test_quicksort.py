import pytest
from load_testdata import load_json_testcases

def quicksort(arr):
        if not arr:
            return []

        pivot = arr[0]
        lesser = quicksort([x for x in arr[1:] if x < pivot])
        # Fix: Include elements equal to the pivot in the 'greater' list.
        greater = quicksort([x for x in arr[1:] if x >= pivot])  
        return lesser + [pivot] + greater


testdata = load_json_testcases(quicksort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_quicksort(input_data, expected):
    assert quicksort(*input_data) == expected
