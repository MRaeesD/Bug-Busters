def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1  # Change is here: Adjust the hi index to the last element.

    while lo <= hi:
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid - 1  # Change is here: Adjust hi index in the 'else' case.

        else:
            lo = mid + 1

    return -1
