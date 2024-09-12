def kheapsort(arr, k):
    import heapq

    heapq.heapify(heap)  # Move this line outside the for loop (change)

    for x in arr:
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)
