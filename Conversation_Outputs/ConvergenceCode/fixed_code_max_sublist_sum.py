def max_sublist_sum(arr):
    # Initialize max_ending_here to the first element of the array
    max_ending_here = arr[0]
    max_so_far = arr[0]  # Initialize max_so_far to the first element as well

    # Iterate through the array starting from the second element
    for x in arr[1:]:
        max_ending_here = max_ending_here + x
        # Reset max_ending_here to x if it becomes negative
        if max_ending_here < 0:
            max_ending_here = x
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far