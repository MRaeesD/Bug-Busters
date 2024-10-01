def flatten(arr):
    for x in arr:
        if isinstance(x, list):
            for y in flatten(x):
                yield y
        else:
            # FIXED: Yield the element 'x' directly.
            yield x