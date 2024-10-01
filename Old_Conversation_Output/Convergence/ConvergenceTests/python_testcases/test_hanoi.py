import pytest
from load_testdata import load_json_testcases

def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        steps.append((start, end))  # Fixed: Should be (start, end)
        steps.extend(hanoi(height - 1, helper, end))
    else:  # Fixed: Added base case for height == 0
        return steps  # Explicitly return the steps list
    return steps


testdata = load_json_testcases(hanoi.__name__)
testdata = [[inp, [tuple(x) for x in out]] for inp, out in testdata]


@pytest.mark.parametrize("input_data,expected", testdata)
def test_hanoi(input_data, expected):
    assert hanoi(*input_data) == expected
