if weight <= j:
                    memo[i, j] = max(
                        memo[i, j],
                        value + memo[i - 1, j - weight]
                    )
