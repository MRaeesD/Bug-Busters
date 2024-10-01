def knapsack(capacity, items):
    from collections import defaultdict
    memo = defaultdict(int)

    for i in range(len(items)):  # Fix: Start from 0 to include all items
        weight, value = items[i]

        for j in range(1, capacity + 1):
            memo[i + 1, j] = memo[i, j]

            if weight <= j:  # Fix: Use <= to include items that exactly fit the capacity
                memo[i + 1, j] = max(
                    memo[i + 1, j],
                    value + memo[i, j - weight]
                )

    return memo[len(items), capacity]