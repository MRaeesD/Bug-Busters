def gcd(a, b):
    if a == 0:  # Adding a zero check for 'a'
        return b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)  # Corrected Recursive Call: Should be gcd(b, a % b)