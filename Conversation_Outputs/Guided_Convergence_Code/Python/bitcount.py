def bitcount(n):
    count = 0
    while n:
        n &= n - 1  # Clear the least significant 1-bit
        count += 1  # Increment count for each 1-bit found
    return count