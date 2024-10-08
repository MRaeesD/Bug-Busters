def powerset(arr):
    if arr:
        first, *rest = arr 
        rest_subsets = powerset(rest)
        # Fix: Prepend subsets without 'first' to maintain order
        return rest_subsets + [[first] + subset for subset in rest_subsets]  
    else:
        return [[]]