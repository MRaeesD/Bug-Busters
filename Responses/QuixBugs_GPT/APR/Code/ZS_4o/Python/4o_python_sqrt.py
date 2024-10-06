def sqrt(x, epsilon):
    approx = x / 2
    while abs(x - approx**2) > epsilon:  # Modify the condition to compare x and approx**2
        approx = 0.5 * (approx + x / approx)
    return approx
