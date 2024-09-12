def max_sublist_sum(arr):
    max_ending_here = 0
    max_so_far = 0

    for x in arr:
        max_ending_here = max(0, max_ending_here + x) # Reset max_ending_here to 0 only if it's negative
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
