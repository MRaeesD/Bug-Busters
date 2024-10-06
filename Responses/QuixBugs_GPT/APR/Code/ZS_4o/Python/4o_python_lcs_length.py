def lcs_length(s, t):
    from collections import Counter

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i > 0 and j > 0:  # Added check to avoid negative indexing
                    dp[i, j] = dp[i - 1, j - 1] + 1  # Modified to correctly reference previous subsequences
                else:
                    dp[i, j] = 1  # Initial match at start of either string
            else:
                dp[i, j] = max(dp[i - 1, j], dp[i, j - 1])  # Ensure propagation of max LCS length

    return max(dp.values()) if dp else 0
