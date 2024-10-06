# Python 3
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0 or not coins:  # Modified condition to also check if coins list is empty
        return 0

    first, *rest = coins
    return possible_change(coins, total - first) + possible_change(rest, total)
