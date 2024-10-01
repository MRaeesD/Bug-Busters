import pytest
from load_testdata import load_json_testcases

# Python 3
def possible_change(coins, total, memo=None):
    if memo is None:
        memo = {}

    # First, check if the coins list is empty
    if not coins:  # Correctly handles empty coins list
        return 0
    
    # Check if the result is already computed and stored in memo
    if (tuple(coins), total) in memo:
        return memo[(tuple(coins), total)]

    if total == 0:
        return 1
    if total < 0:
        return 0

    first, *rest = coins
    result = possible_change(coins, total - first, memo) + possible_change(rest, total, memo)

    # Store the result in memo before returning
    memo[(tuple(coins), total)] = result
    return result

# Example usage:
print(possible_change([1, 5, 10, 25], 11))  # Output should be 4


testdata = load_json_testcases(possible_change.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_possible_change(input_data, expected):
    assert possible_change(*input_data) == expected
