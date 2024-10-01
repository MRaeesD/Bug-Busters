import pytest
from load_testdata import load_json_testcases

def shunting_yard(tokens):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    rpntokens = []
    opstack = []
    for token in tokens:
        if isinstance(token, int):
            rpntokens.append(token)
        elif token == '(':
            opstack.append(token)  # Handle opening parenthesis
        elif token == ')':
            while opstack and opstack[-1] != '(':
                rpntokens.append(opstack.pop())
            opstack.pop()  # Pop the '(' from the stack
        else:
            while opstack and precedence[token] <= precedence[opstack[-1]]:
                rpntokens.append(opstack.pop())
            opstack.append(token)  # Push the current operator onto the stack

    while opstack:
        rpntokens.append(opstack.pop())

    return rpntokens

# The code now includes logic to handle parentheses, ensures the current operator is pushed onto the opstack, 
# and correctly processes the operator stack.


testdata = load_json_testcases(shunting_yard.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_shunting_yard(input_data, expected):
    assert shunting_yard(*input_data) == expected
