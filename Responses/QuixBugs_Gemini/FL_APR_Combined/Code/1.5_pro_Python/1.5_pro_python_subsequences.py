def subsequences(a, b, k):
        if k == 0:
            return []

        ret = []
        for i in range(a, b + 1 - k):
            # Fix: Use a list comprehension to generate the lists before extending
            ret.extend(
                [i] + rest for rest in subsequences(i + 1, b, k - 1)
            )

        return ret
