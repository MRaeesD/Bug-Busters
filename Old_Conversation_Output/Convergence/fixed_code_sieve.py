def sieve(max):
    if max < 2:  # Handle case where max is less than 2
        return []
    
    primes = []
    for n in range(2, max + 1):
        # Correct the prime identification logic
        if all(n % p != 0 for p in primes):
            primes.append(n)
    return primes