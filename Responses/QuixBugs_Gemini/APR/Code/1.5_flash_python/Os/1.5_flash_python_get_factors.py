def get_factors(n):
    if n == 1:
        return []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(i) + get_factors(n // i)  # Change is here

    return [n]  # Include the number itself if it's prime
