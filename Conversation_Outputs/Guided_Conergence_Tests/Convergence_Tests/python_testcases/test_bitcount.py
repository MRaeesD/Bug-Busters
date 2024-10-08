import pytest
from load_testdata import load_json_testcases

def bitcount(n):
    count = 0
    while n:
        n &= n - 1  # Clear the least significant 1-bit
        count += 1  # Increment count for each 1-bit found
    return count

testdata = load_json_testcases(bitcount.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_bitcount(input_data, expected):
    assert bitcount(*input_data) == expected
