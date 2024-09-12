def bitcount(n):
    count = 0
    while n:
        count += n & 1 # Corrected line: Count the least significant bit directly
        n >>= 1 # Right shift 'n' to check the next bit in the next iteration
    return count
