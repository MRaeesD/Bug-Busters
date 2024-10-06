import pytest
from load_testdata import load_json_testcases

def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if not any(n % p == 0 for p in primes):
            primes.append(n)
    return primes


testdata = load_json_testcases(sieve.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_sieve(input_data, expected):
    assert sieve(*input_data) == expected
