def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):  # Fixed to iterate over 'counts'
        if count > 0:  # Added condition to check if count is greater than zero
            sorted_arr.extend([i] * count)

    return sorted_arr