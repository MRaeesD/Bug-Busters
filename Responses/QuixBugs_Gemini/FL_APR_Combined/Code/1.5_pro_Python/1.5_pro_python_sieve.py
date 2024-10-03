def sieve(max):
        primes = []
        for n in range(2, max + 1):
            # Fix: Check if n is NOT divisible by any existing prime
            if all(n % p != 0 for p in primes): 
                primes.append(n)
        return primes
