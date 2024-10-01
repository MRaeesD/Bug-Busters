def get_factors(n):
    if n == 1:
        return []  # Correctly returns an empty list for the input 1

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)  # Continue factoring by recursively calling the function

    return [n] if n > 1 else []  # Return [n] if n is prime, ensuring all cases are handled