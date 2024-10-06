def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if all(n % p > 0 for p in primes):  # Changed `any` to `all`
            primes.append(n)
    return primes
