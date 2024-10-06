def sqrt(x, epsilon):
    approx = x / 2
    while abs(x - approx * approx) > epsilon:  # Change made here
        approx = 0.5 * (approx + x / approx)
    return approx
