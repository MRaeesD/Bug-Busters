import pytest
from load_testdata import load_json_testcases

def kheapsort(arr, k):
    import heapq  # Moved import statement to the top for better readability

    # Initialize the heap with the first k+1 elements
    heap = arr[:k+1]
    heapq.heapify(heap)

    # Iterate over the remaining elements in the array
    for x in arr[k+1:]:
        yield heapq.heappushpop(heap, x)

    # Extract remaining elements from the heap
    while heap:
        yield heapq.heappop(heap)


testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
