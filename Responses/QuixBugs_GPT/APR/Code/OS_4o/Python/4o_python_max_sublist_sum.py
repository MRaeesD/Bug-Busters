def max_sublist_sum(arr):
    max_ending_here = 0
    max_so_far = 0

    for x in arr:
        max_ending_here = max_ending_here + x  # Add current element to max_ending_here
        max_ending_here = max(max_ending_here, 0)  # Correct the bug: reset to 0 if negative
        max_so_far = max(max_so_far, max_ending_here)  # Update max_so_far if needed

    return max_so_far
