import pytest
from load_testdata import load_json_testcases

import heapq
def kheapsort(arr, k):
    # Handle the case when k is greater than or equal to the length of the array
    if k >= len(arr):
        k = len(arr) - 1
    heap = arr[:k + 1]  # Bug fix: Include the first k+1 elements in the heap
    heapq.heapify(heap)
    result = []  # Store sorted elements
    for i in range(k + 1, len(arr)):  # Bug fix: Iterate from k+1th element
        result.append(heapq.heappushpop(heap, arr[i]))
    while heap:
        result.append(heapq.heappop(heap))
    for x in result:  # Yield from the sorted result
        yield x


testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
