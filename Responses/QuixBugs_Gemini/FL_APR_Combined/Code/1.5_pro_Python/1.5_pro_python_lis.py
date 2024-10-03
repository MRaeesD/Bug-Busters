def lis(arr):
        ends = {}
        longest = 0

        for i, val in enumerate(arr):

            # Fix 1: Check if j is in ends before accessing
            prefix_lengths = [j for j in range(1, longest + 1) if j in ends and arr[ends[j]] < val]

            length = max(prefix_lengths) if prefix_lengths else 0

            # Fix 2: Check if length + 1 is in ends before accessing
            if length == longest or (length + 1 in ends and val < arr[ends[length + 1]]): 
                ends[length + 1] = i
                longest = length + 1

        return longest
