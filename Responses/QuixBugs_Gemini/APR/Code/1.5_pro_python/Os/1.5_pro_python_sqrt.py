def sqrt(x, epsilon):
    approx = x / 2
    while abs(approx * approx - x) > epsilon: # Fix is on this line
        approx = 0.5 * (approx + x / approx)
    return approx
