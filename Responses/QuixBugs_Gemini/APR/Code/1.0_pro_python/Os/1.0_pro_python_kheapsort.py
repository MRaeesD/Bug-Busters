for x in arr[k:]:
        # Changed the range to start from k
        yield heapq.heappushpop(heap, x)
