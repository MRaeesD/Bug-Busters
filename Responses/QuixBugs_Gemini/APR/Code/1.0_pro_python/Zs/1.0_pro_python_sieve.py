def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if any(n % p == 0 for p in primes):  # Change from n % p > 0 to n % p == 0
            primes.append(n)
    return primes
