import pytest
from load_testdata import load_json_testcases

def bitcount(n):
    count = 0
    while n:
        n ^= n - 1  # No change needed, this line efficiently removes the rightmost set bit
        count += 1
    return count



testdata = load_json_testcases(bitcount.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_bitcount(input_data, expected):
    assert bitcount(*input_data) == expected
