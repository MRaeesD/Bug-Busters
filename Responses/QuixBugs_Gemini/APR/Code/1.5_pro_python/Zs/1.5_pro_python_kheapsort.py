def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    for x in arr[k:]: # Start iteration from the kth element
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)
