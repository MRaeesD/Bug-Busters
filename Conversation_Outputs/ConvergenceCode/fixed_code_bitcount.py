def bitcount(n):
    count = 0
    while n:
        count += n & 1  # Check the least significant bit
        n >>= 1         # Right shift n by 1 to check the next bit
    return count