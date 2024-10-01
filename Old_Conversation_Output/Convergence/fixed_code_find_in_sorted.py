def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start > end:
            return -1  # Adjusted base case to handle when start is greater than end
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid - 1)  # Adjusted to mid - 1
        elif x > arr[mid]:
            return binsearch(mid + 1, end)  # Adjusted to mid + 1
        else:
            return mid

    return binsearch(0, len(arr) - 1)  # Adjusted end to len(arr) - 1 