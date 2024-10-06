import pytest
from load_testdata import load_json_testcases

def is_valid_parenthesization(parens):
        depth = 0
        for paren in parens:
            if paren == '(':
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    return False
        # Check if depth is 0 at the end 
        return depth == 0 # Fixed Code



testdata = load_json_testcases(is_valid_parenthesization.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_is_valid_parenthesization(input_data, expected):
    assert is_valid_parenthesization(*input_data) == expected
