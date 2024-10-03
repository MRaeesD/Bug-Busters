def flatten(arr):
        for x in arr:
            if isinstance(x, list):
                for y in flatten(x):
                    yield y
            else:
                yield x # Fixed: Removed the erroneous call to 'flatten(x)' and replaced it with 'yield x' to yield the non-list element directly.
