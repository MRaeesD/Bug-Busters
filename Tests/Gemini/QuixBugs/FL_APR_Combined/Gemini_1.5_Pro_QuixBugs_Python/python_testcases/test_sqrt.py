import pytest
from load_testdata import load_json_testcases

def sqrt(x, epsilon):
    """
    Calculate the square root of a number using the Newton-Raphson method.

    Args:
        x: The number to calculate the square root of.
        epsilon: The desired accuracy.

    Returns:
        The square root of x within the specified accuracy.
    """
    approx = x / 2
    # Fix: Changed the condition in while to check the difference between the square of the approximation and x
    while abs(approx * approx - x) > epsilon: 
        approx = 0.5 * (approx + x / approx)
    return approx



testdata = load_json_testcases(sqrt.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_sqrt(input_data, expected):
    assert sqrt(*input_data) == pytest.approx(expected, abs=input_data[-1])
