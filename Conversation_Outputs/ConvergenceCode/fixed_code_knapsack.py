def knapsack(capacity, items):
    from collections import defaultdict
    memo = defaultdict(int)

    for i in range(len(items)):  # Changed to range(len(items)) to include all items
        weight, value = items[i]

        for j in range(capacity + 1):  # Changed to range(capacity + 1) to include capacity 0
            memo[i, j] = memo[i - 1, j]

            if weight <= j:  # Adjusted condition to weight <= j to include items with weight exactly equal to capacity
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items) - 1, capacity]  # Adjusted to len(items) - 1 to correctly reference the last item