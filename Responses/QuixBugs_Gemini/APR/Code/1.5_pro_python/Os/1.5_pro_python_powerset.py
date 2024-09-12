def powerset(arr):
    if arr:
        first, *rest = arr 
        rest_subsets = powerset(rest)
        return [[first] + subset for subset in rest_subsets] + rest_subsets # Include subsets from the 'rest' of the list
    else:
        return [[]]
