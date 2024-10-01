def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        # Fix: Include both subsets that include 'first' and those that do not
        return rest_subsets + [[first] + subset for subset in rest_subsets]
    else:
        return [[]]