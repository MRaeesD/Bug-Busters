def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends.get(j, -1)] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends.get(length + 1, -1)]:
            ends[length + 1] = i
            if length + 1 > longest:  # bug fix: update longest only if length + 1 is greater
                longest = length + 1

    return longest