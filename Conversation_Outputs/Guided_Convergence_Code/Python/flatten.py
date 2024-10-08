def flatten(arr):
    for x in arr:
        if isinstance(x, list):
            for y in flatten(x):
                yield y
        else:
            yield x  # Fix: Directly yield the non-list object instead of calling flatten on a non-list object