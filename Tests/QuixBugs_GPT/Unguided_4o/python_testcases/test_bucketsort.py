import pytest
from load_testdata import load_json_testcases

def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):
        sorted_arr.extend([i] * count)

    return sorted_arr


testdata = load_json_testcases(bucketsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_bucketsort(input_data, expected):
    assert bucketsort(*input_data) == expected
