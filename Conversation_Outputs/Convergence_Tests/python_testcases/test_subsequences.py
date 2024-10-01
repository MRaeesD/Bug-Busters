import pytest
from load_testdata import load_json_testcases

def subsequences(a, b, k):
    if k == 0:
        return [[]]  # Bug fixed: Base case should return [[]] instead of []

    ret = []
    for i in range(a, b - k + 2):  # Bug fixed: Adjusted range to correctly iterate over all starting points
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret


testdata = load_json_testcases(subsequences.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_subsequences(input_data, expected):
    assert subsequences(*input_data) == expected
