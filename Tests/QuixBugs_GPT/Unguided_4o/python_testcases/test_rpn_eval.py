import pytest
from load_testdata import load_json_testcases

def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, (float, int)):  # Fix to accept both float and int
            stack.append(token)
        else:
            b = stack.pop()  # Fix order: pop second operand first
            a = stack.pop()  # pop first operand
            stack.append(
                op(token, a, b)
            )

    return stack.pop()

testdata = load_json_testcases(rpn_eval.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_rpn_eval(input_data, expected):
    assert rpn_eval(*input_data) == expected
