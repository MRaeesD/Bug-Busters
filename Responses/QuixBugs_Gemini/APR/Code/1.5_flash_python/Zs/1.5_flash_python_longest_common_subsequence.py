def longest_common_subsequence(a, b):
    if not a or not b:
        return ''

    elif a[0] == b[0]:
        # Change: return the first character plus the longest common subsequence of the remaining strings
        return a[0] + longest_common_subsequence(a[1:], b[1:]) 

    else:
        return max(
            longest_common_subsequence(a, b[1:]),
            longest_common_subsequence(a[1:], b),
            key=len
        )
