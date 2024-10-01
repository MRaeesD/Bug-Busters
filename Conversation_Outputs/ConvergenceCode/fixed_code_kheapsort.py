def kheapsort(arr, k):
    import heapq

    heap = arr[:k + 1]  # Initialize with arr[:k+1] to cover the range of k displacements
    heapq.heapify(heap)

    for x in arr[k + 1:]:  # Start iterating from arr[k+1:] to handle elements beyond the initial k+1
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)