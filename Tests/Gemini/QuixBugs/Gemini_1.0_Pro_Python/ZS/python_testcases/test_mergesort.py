import pytest
from load_testdata import load_json_testcases

def mergesort(arr):
    def merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:] or right[j:])
        return result

    if len(arr) == 0:
        return []  # Change made here
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)


testdata = load_json_testcases(mergesort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_mergesort(input_data, expected):
    assert mergesort(*input_data) == expected
