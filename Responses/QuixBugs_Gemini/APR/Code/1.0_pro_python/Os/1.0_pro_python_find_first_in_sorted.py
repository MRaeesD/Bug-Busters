while lo < hi:
    # Change made here: change while lo <= hi: to while lo < hi:
    mid = (lo + hi) // 2

    if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
        return mid

    elif x <= arr[mid]:
        hi = mid

    else:
        lo = mid + 1

return -1
