def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    # Iterate through the array only up to k elements ahead of the current heap position
    for i in range(k, len(arr)):  
        yield heapq.heappushpop(heap, arr[i])

    while heap:
        yield heapq.heappop(heap)
