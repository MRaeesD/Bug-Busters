import pytest
from load_testdata import load_json_testcases

def get_factors(n):
    if n == 1:
        return []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)

    return [n]  # Bug fix: Return the number itself if it's prime


testdata = load_json_testcases(get_factors.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_get_factors(input_data, expected):
    assert get_factors(*input_data) == expected
