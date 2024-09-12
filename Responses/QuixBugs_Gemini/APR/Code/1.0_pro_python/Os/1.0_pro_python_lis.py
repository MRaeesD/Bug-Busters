if length == longest or val < arr[ends[length + 1]]:
    ends[length + 1] = i
    longest = max(length + 1, longest)   # Change made
