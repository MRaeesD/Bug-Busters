def bitcount(n):
    count = 0
    while n:
        n &= n - 1  # Corrected line
        count += 1
    return count
