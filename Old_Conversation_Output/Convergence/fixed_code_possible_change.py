# Python 3
def possible_change(coins, total):
    # Base case: if total is 0, there is exactly one way to make change (using no coins)
    if total == 0:
        return 1
    # Base case: if total is negative, there is no way to make change
    if total < 0:
        return 0
    # Base case: if there are no coins left and total is still positive, no way to make change 
    if not coins: # Bug fix: Added base case for an empty coin list
        return 0

    first, *rest = coins
    # Recursive calls:
    # 1. Include the first coin and reduce the total by the value of the first coin
    # 2. Exclude the first coin and move to the rest of the coins
    return possible_change(coins, total - first) + possible_change(rest, total)

# Example usage:
print(possible_change([1, 5, 10, 25], 11))  # Output: 4