def flatten(arr):
    for x in arr:
        if isinstance(x, list):
            for y in flatten(x):
                yield y
        else:
            # BUG FIX: Yield the element x directly instead of calling flatten on a non-list
            yield x

# Example usage:
print(list(flatten([[1, [], [2, 3]], [[4]], 5])))  # Output should be [1, 2, 3, 4, 5]