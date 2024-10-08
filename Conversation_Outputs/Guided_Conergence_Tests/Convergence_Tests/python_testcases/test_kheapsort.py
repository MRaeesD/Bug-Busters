import pytest
from load_testdata import load_json_testcases

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


testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
