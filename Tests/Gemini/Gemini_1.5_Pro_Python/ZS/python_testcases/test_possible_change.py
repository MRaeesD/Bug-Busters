import pytest
from load_testdata import load_json_testcases

# Python 3
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(coins) == 0: # added base case to handle empty coin list
        return 0

    first, *rest = coins
    return possible_change(coins, total - first) + possible_change(rest, total)



testdata = load_json_testcases(possible_change.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_possible_change(input_data, expected):
    assert possible_change(*input_data) == expected
