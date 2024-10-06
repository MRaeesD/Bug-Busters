def bitcount(n):
    count = 0
    while n:
        n &= (n - 1)  # Changed from ^= to &= to ensure that only the last set bit is turned off
        count += 1
    return count
