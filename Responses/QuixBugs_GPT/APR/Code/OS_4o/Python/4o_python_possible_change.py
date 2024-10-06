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
