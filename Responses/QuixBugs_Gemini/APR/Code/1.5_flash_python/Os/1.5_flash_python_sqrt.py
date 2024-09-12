def sqrt(x, epsilon):
    approx = x / 2
    while abs(approx**2 - x) > epsilon:  # Change is made here
        approx = 0.5 * (approx + x / approx)
    return approx
