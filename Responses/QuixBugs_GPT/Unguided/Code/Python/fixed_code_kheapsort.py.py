def kheapsort(arr, k):
    import heapq

    # Initialize the heap with the first k+1 elements
    heap = arr[:k+1]
    heapq.heapify(heap)

    # Iterate over the remaining elements, if any
    for x in arr[k+1:]:
        yield heapq.heappushpop(heap, x)

    # Extract all remaining elements from the heap
    while heap:
        yield heapq.heappop(heap)