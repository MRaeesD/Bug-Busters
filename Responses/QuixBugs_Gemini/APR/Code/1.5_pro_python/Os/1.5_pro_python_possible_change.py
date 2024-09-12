# Python 3
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0 or not coins: # Added check for an empty coin list
        return 0

    first, *rest = coins
    return possible_change(coins, total - first) + possible_change(rest, total)
