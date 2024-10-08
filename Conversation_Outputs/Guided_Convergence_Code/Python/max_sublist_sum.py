def max_sublist_sum(arr):
    max_ending_here = 0
    max_so_far = 0

    for x in arr:
        # If max_ending_here becomes negative, reset it to 0
        max_ending_here = max(0, max_ending_here + x) 
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far