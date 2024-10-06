def lcs_length(s, t):
    from collections import Counter

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i - 1 < 0 or (i - 1, j) not in dp:  # Check if (i - 1, j) is valid in the dp Counter
                    dp[i, j] = 1
                else:
                    dp[i, j] = dp[i - 1, j] + 1

    return max(dp.values()) if dp else 0
