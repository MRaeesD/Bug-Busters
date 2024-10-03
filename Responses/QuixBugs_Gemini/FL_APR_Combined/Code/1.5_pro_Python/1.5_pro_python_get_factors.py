def get_factors(n):
        if n == 1:
            return []

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                # Fix: Recursively find factors of the remaining quotient (n//i) 
                # and append them to the list along with the current factor (i).
                return [i] + get_factors(n // i)  

        # Fix: If no factors are found in the loop, 'n' itself is a prime factor.
        return [n]
