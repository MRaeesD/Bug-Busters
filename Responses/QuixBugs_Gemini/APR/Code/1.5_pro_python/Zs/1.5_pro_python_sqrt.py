def sqrt(x, epsilon):
    if x == 0:  # Handle the case when x is 0
        return 0
    approx = x / 2
    while abs(x - approx**2) > epsilon: #Change made in this line 
        approx = 0.5 * (approx + x / approx)
    return approx
