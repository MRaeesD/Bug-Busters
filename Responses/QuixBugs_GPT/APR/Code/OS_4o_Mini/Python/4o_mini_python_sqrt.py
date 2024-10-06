def sqrt(x, epsilon):
    approx = x / 2
    # Change made here
    while abs(approx * approx - x) > epsilon:
        approx = 0.5 * (approx + x / approx)
    return approx
