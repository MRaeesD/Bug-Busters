def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if all(n % p > 0 for p in primes): # Use all instead of any
            primes.append(n)
    return primes
