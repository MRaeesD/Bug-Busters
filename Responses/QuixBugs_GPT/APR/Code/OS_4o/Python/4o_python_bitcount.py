def bitcount(n):
    count = 0
    while n:
        n &= n - 1  # This operation removes the least significant 1-bit
        count += 1
    return count
