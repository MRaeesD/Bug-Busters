def sqrt(x, epsilon):
    approx = x / 2
    while abs(approx * approx - x) > epsilon:  # Changed condition to check the difference between the square of the approximation and x
        approx = 0.5 * (approx + x / approx)
    return approx
