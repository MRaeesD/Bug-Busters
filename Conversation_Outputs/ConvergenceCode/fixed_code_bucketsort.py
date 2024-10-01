def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):  # Fixed the loop to iterate over 'counts'
        sorted_arr.extend([i] * count)  # Extend the sorted array with the element 'i', 'count' times

    return sorted_arr  # Return the sorted array