def sqrt(x, epsilon):
    # Precondition checks
    assert x >= 1, "x should be greater than or equal to 1"
    assert epsilon > 0, "epsilon should be greater than 0"

    approx = x / 2
    max_iterations = 1000
    iterations = 0

    # Corrected while loop condition
    while abs(approx**2 - x) > epsilon:
        approx = 0.5 * (approx + x / approx)
        iterations += 1
        if iterations >= max_iterations:
            break  # Safeguard against infinite loop

    return approx