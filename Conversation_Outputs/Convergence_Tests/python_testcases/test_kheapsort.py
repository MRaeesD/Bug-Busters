import pytest
from load_testdata import load_json_testcases

def kheapsort(arr, k):
    import heapq

    heap = arr[:k + 1]  # Initialize with arr[:k+1] to cover the range of k displacements
    heapq.heapify(heap)

    for x in arr[k + 1:]:  # Start iterating from arr[k+1:] to handle elements beyond the initial k+1
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)


testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
