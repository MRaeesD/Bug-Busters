def gcd(a, b):
        if b == 0:
            return a
        else:
            # The arguments were swapped. It should be (b, a % b)
            return gcd(b, a % b) # Bug fix
