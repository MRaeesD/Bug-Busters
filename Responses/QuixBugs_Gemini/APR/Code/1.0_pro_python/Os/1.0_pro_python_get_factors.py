def get_factors(n):
    if n == 1:
        return []  # The return statement is modified here
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)

    return [n] # The return statement is added here
