import pytest
from load_testdata import load_json_testcases

def sqrt(x, epsilon):
    approx = x / 2
    while abs(approx * approx - x) > epsilon:
        approx = 0.5 * (approx + x / approx)
    return approx

testdata = load_json_testcases(sqrt.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_sqrt(input_data, expected):
    assert sqrt(*input_data) == pytest.approx(expected, abs=input_data[-1])
