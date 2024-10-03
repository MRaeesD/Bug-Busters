def possible_change(coins, total):
        if total == 0:
            return 1
        if total < 0:
            return 0
        if not coins:
            return 0

        first, *rest = coins
        # Use 'rest' instead of 'coins' in the first recursive call
        return possible_change(rest, total - first) + possible_change(rest, total)
