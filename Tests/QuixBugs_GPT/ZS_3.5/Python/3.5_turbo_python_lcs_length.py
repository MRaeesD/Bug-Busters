def lcs_length(s, t):
    from collections import Counter

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if i == 0 or j == 0:
                dp[i, j] = 1 if s[i] == t[j] else 0
            elif s[i] == t[j]:
                dp[i, j] = dp[i - 1, j - 1] + 1
    return max(dp.values()) if dp else 0
