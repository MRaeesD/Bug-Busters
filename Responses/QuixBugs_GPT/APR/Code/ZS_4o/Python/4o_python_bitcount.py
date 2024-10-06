def bitcount(n):
    count = 0
    while n:
        n &= n - 1  # Corrected this line
        count += 1
    return count
