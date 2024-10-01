def kth(arr, k):
    # Base case: if the array has only one element, return it
    if len(arr) == 1:
        return arr[0]

    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]  # Handle elements equal to the pivot

    num_less = len(below)
    num_lessoreq = len(below) + len(equal)  # Correct calculation including equal elements

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k - num_lessoreq)  # Fixed: index adjustment
    else:
        return pivot