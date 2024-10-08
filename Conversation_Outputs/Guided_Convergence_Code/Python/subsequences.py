def subsequences(a, b, k):
    if k == 0:
        return [[]]  # Fixed: Return a list containing an empty list for the base case 
    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret