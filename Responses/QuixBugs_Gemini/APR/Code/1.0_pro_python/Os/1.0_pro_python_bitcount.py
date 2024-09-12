def bitcount(n):
    count = 0
    while n:
        n &= n - 1  # Corrected this line from n ^= n - 1 to n &= n - 1
        count += 1
    return count
