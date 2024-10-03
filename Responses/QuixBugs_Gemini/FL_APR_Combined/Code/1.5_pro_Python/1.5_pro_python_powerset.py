def powerset(arr):
        if arr:
            first, *rest = arr
            rest_subsets = powerset(rest)
            # Include subsets with and without 'first'
            return rest_subsets + [[first] + subset for subset in rest_subsets]  # Fix: Add 'rest_subsets +' to include subsets without 'first'
        else:
            return [[]]
