def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    for x in arr[k:]:  # Change made here to start iteration from k-th element
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)
