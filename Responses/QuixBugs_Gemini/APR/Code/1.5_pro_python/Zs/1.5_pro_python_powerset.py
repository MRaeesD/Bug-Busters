def powerset(arr):
    if arr:
        first, *rest = arr 
        rest_subsets = powerset(rest)
        return rest_subsets + [[first] + subset for subset in rest_subsets] # Include both subsets with and without 'first'
    else:
        return [[]]
