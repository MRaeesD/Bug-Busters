import pytest
from load_testdata import load_json_testcases

def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    # Iterate through the array only up to k elements ahead of the current heap position
    for i in range(k, len(arr)):  
        yield heapq.heappushpop(heap, arr[i])

    while heap:
        yield heapq.heappop(heap)


testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
