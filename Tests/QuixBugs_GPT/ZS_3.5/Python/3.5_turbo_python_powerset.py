def powerset(arr):
    if arr:
        first, *rest = arr 
        rest_subsets = powerset(rest)
        if rest_subsets: # check if rest_subsets is not empty
            return [[first] + subset for subset in rest_subsets]
        return [[first]] + rest_subsets # return [first] as a subset when rest_subsets is empty 
    else:
        return [[]]
