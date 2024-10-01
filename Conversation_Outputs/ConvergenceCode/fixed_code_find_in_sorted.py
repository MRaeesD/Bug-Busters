def find_in_sorted(arr, x):
    # Handle the edge case where the input array is empty
    if not arr:
        return -1

    def binsearch(start, end):
        # Correct the termination condition
        if start >= end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            # Correct the range for the recursive call
            return binsearch(mid + 1, end)
        else:
            return mid

    return binsearch(0, len(arr))

# Test cases to validate the implementation
def test_find_in_sorted():
    assert find_in_sorted([3, 4, 5, 5, 5, 5, 6], 5) == 3
    assert find_in_sorted([1, 2, 3, 4, 5], 6) == -1
    assert find_in_sorted([], 1) == -1
    assert find_in_sorted([1], 1) == 0
    assert find_in_sorted([1], 2) == -1
    assert find_in_sorted([1, 2, 3, 4, 5], 1) == 0
    assert find_in_sorted([1, 2, 3, 4, 5], 5) == 4
    assert find_in_sorted([-5, -3, -1, 0, 2, 4, 6], -3) == 1
    print("All test cases pass")

# Run the test cases
test_find_in_sorted()