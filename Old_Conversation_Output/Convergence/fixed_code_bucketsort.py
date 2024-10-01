def bucketsort(arr, k):
    # Initialize counts array
    counts = [0] * k
    
    # Count the occurrences of each element in arr
    for x in arr:
        counts[x] += 1

    # Construct the sorted array based on counts
    sorted_arr = []
    for i, count in enumerate(counts):  # Iterate over counts
        for _ in range(count):  # Add the correct element value
            sorted_arr.append(i)  # Append the actual value i

    return sorted_arr