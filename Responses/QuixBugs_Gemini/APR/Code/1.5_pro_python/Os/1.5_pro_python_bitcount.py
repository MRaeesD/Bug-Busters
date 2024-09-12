def bitcount(n):
    count = 0
    while n:
        n ^= n - 1  # No change needed, this line efficiently removes the rightmost set bit
        count += 1
    return count
