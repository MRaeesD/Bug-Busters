def kheapsort(arr, k):
    import heapq

    heap = arr[:k]  # Initial k elements
    heapq.heapify(heap)

    for x in arr[k:]:  # Start from the (k+1)-th element
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)
