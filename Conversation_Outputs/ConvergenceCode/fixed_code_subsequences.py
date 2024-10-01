def subsequences(a, b, k):
    if k == 0:
        return [[]]  # Bug fixed: Base case should return [[]] instead of []

    ret = []
    for i in range(a, b - k + 2):  # Bug fixed: Adjusted range to correctly iterate over all starting points
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret