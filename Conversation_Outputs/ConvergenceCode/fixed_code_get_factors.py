def get_factors(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be an integer greater than or equal to 1")

    if n == 1:
        return []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)

    return [n]  # Fix: Return [n] if n is prime