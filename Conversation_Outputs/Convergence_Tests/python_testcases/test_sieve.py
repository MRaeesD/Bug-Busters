import pytest
from load_testdata import load_json_testcases

def sieve(max):
    primes = [2]  # Initialize the list with the first prime number
    for n in range(3, max + 1):  # Start from 3 since 2 is already included
        if all(n % p != 0 for p in primes):  # Correct logic to check for prime
            primes.append(n)
    return primes


testdata = load_json_testcases(sieve.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_sieve(input_data, expected):
    assert sieve(*input_data) == expected
