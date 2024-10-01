import pytest
from load_testdata import load_json_testcases

def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b  # Consider if integer division is needed.
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, (int, float)):  # Fix: Check for both integers and floats.
            stack.append(token)
        else:
            if len(stack) < 2:  # Fix: Check to prevent stack underflow.
                raise ValueError("Insufficient operands in the stack.")
            b = stack.pop()  # Fix: Correct order of operand retrieval.
            a = stack.pop()
            stack.append(
                op(token, a, b)  # Fix: Operands are now passed in the correct order.
            )

    if len(stack) != 1:  # Fix: Ensure there's exactly one element left in the stack.
        raise ValueError("The input tokens do not form a valid RPN expression.")

    return stack.pop()


testdata = load_json_testcases(rpn_eval.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_rpn_eval(input_data, expected):
    assert rpn_eval(*input_data) == expected
