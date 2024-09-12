def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if all(n % p != 0 for p in primes): # Corrected condition: Check if n is NOT divisible by any existing prime
            primes.append(n)
    return primes
