import pytest
from load_testdata import load_json_testcases

def bitcount(n):
    count = 0
    while n:
        count += n & 1  # Check the least significant bit
        n >>= 1         # Right shift n by 1 to check the next bit
    return count


testdata = load_json_testcases(bitcount.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_bitcount(input_data, expected):
    assert bitcount(*input_data) == expected
