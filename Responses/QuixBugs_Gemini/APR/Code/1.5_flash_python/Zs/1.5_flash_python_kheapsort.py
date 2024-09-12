def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    # Iterate through the rest of the array starting from index k
    for x in arr[k:]: 
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)
