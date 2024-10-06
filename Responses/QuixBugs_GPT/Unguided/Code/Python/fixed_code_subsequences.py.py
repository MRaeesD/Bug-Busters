def subsequences(a, b, k):
        if k == 0:
            return [[]]  # Return a list of an empty list to allow recursion to return proper sublists

        ret = []
        for i in range(a, b + 1 - k + 1):  # Correct the loop to include the end range and ensure valid subsequences
            ret.extend(
                [[i] + rest for rest in subsequences(i + 1, b, k - 1)]
            )

        return ret