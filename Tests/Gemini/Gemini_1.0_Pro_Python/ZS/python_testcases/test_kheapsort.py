import pytest
from load_testdata import load_json_testcases

def kheapsort(arr, k):
    import heapq

    heapq.heapify(heap)  # Move this line outside the for loop (change)

    for x in arr:
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)


testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
