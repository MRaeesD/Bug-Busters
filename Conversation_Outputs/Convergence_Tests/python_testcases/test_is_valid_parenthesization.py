import pytest
from load_testdata import load_json_testcases

def is_valid_parenthesization(parens):
    """
    Check if a string of parentheses is properly nested.

    Args:
    parens (str): A string consisting of '(' and ')' characters.

    Returns:
    bool: True if the parentheses are properly nested, False otherwise.

    Properly nested parentheses mean:
    - Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
    - The closing parenthesis should not appear before its matching opening parenthesis.
    - At the end of the string, the number of opening and closing parentheses should be equal.
    """
    depth = 0
    for paren in parens:
        if paren == '(':
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                return False

    # Bug fix: Check if depth is zero at the end
    return depth == 0  # All opening parentheses should have a matching closing one


testdata = load_json_testcases(is_valid_parenthesization.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_is_valid_parenthesization(input_data, expected):
    assert is_valid_parenthesization(*input_data) == expected
