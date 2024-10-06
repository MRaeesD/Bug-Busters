import pytest
from load_testdata import load_json_testcases

def kheapsort(arr, k):
    import heapq

    heap = arr[:k + 1]  # Include the first k + 1 elements for the initial heap
    heapq.heapify(heap)

    for x in arr[k + 1:]:  # Iterate over the remainder of the array
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)



testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
