def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)  # Changed the order of parameters here
