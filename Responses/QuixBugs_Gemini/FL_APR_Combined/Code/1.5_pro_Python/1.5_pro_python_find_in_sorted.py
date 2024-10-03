def find_in_sorted(arr, x):
        def binsearch(start, end):
            if start >= end:  # Fix 1: Ensure we check the last element in a segment
                return -1
            mid = start + (end - start) // 2
            if x < arr[mid]:
                return binsearch(start, mid) # Fix 3: Correctly limit the search space
            elif x > arr[mid]:
                return binsearch(mid + 1, end) # Fix 2: Start from 'mid + 1'
            else:
                return mid

        return binsearch(0, len(arr))
