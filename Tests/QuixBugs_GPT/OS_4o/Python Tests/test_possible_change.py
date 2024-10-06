import pytest
from load_testdata import load_json_testcases

# Python 3
def possible_change(coins, total, index=0, memo=None):
    if total == 0:
        return 1
    if total < 0 or index == len(coins):
        return 0
    if memo is None:
        memo = {}
    if (total, index) in memo:
        return memo[(total, index)]
    
    with_current_coin = possible_change(coins, total - coins[index], index, memo)
    without_current_coin = possible_change(coins, total, index + 1, memo)

    memo[(total, index)] = with_current_coin + without_current_coin
    return memo[(total, index)]



testdata = load_json_testcases(possible_change.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_possible_change(input_data, expected):
    assert possible_change(*input_data) == expected
