def bitcount(n):
    count = 0
    while n:
        # Change: Use n & (n - 1) to clear the rightmost set bit
        n &= n - 1 
        count += 1
    return count
