def sqrt(x, epsilon):
    approx = x / 2
    while abs(approx * approx - x) > epsilon:  # Changed the condition to compare approximations
        approx = 0.5 * (approx + x / approx)
    return approx
