def kheapsort(arr, k):
    import heapq

    # Boundary check for k 
    if k >= len(arr): 
        for x in sorted(arr):
            yield x
        return

    heap = arr[:k + 1]  # Bugfix: Initialize with k+1 elements 
    heapq.heapify(heap)

    for x in arr[k + 1:]:  # Bugfix: Start loop from (k+1)th element
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)