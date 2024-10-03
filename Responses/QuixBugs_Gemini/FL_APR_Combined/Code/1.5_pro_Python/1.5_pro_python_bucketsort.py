def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):  # Iterate through counts array
        sorted_arr.extend([i] * count)  # Use bucket index 'i'

    return sorted_arr
