import pytest
from load_testdata import load_json_testcases

import string

def to_base(num, b):
    result = ''
    alphabet = string.digits + string.ascii_uppercase
    while num > 0:
        i = num % b
        num = num // b
        result = alphabet[i] + result  # Fix: Prepend to result, not append
    return result


testdata = load_json_testcases(to_base.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_to_base(input_data, expected):
    assert to_base(*input_data) == expected
