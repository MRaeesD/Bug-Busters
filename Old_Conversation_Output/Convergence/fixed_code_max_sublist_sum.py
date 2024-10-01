def max_sublist_sum(arr):
    if not arr:
        return 0  # Handle empty array case
    
    max_ending_here = arr[0]  # Initialize to the first element of the array
    max_so_far = arr[0]  # Initialize to the first element of the array

    for x in arr[1:]:  # Start from the second element
        max_ending_here = max(x, max_ending_here + x)  # Reset if max_ending_here becomes negative
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far