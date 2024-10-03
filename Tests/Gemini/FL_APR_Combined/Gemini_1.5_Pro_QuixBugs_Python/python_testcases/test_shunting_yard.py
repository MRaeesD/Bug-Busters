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
            elif token in '+-*/': # Bug fix: Check if token is an operator
                # Bug fix: Handle operators correctly within the while loop
                while opstack and opstack[-1] != '(' and precedence[token] <= precedence[opstack[-1]]:
                    rpntokens.append(opstack.pop())
                opstack.append(token) # Bug fix: Push the operator onto the opstack
            elif token == '(':
                opstack.append(token)
            elif token == ')':
                while opstack and opstack[-1] != '(':
                    rpntokens.append(opstack.pop())
                opstack.pop() # Discard the '('

        while opstack:
            rpntokens.append(opstack.pop())

        return rpntokens


testdata = load_json_testcases(shunting_yard.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_shunting_yard(input_data, expected):
    assert shunting_yard(*input_data) == expected
