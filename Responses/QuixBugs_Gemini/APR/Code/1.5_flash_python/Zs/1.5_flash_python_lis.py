Fix:

def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        # Update longest only if length is greater
        if length > longest:  
            ends[length + 1] = i
            longest = length + 1

    return longest
