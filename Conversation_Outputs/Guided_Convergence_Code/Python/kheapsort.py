def kheapsort(arr, k):
    import heapq

    # Initialize the heap with the first k elements
    heap = arr[:k]
    heapq.heapify(heap)

    # Start iterating from the k-th element since the first k elements are already in the heap
    for x in arr[k:]:
        yield heapq.heappushpop(heap, x)

    # Yield the remaining elements in the heap
    while heap:
        yield heapq.heappop(heap)