import pytest
from load_testdata import load_json_testcases

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)  # Fixed the argument order


testdata = load_json_testcases(gcd.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_gcd(input_data, expected):
    assert gcd(*input_data) == expected
