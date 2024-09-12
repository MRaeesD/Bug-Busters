def lcs_length(s, t):
    from collections import Counter

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i, j] = dp[i, j - 1] + 1  # Change here to dp[i, j - 1]

    return max(dp.values()) if dp else 0
