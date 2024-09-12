if total == 0:
    return 1
if total < 0 or not coins:
    return 0  # Added a check for an empty list of coins

first, *rest = coins
return possible_change(coins, total - first) + possible_change(rest, total)
