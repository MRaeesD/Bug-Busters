import random

def kth(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    below = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)

    if k < num_less:
        return kth(below, k)
    elif k < num_less + len(equal):
        return pivot
    else:
        return kth(above, k - num_less - len(equal))