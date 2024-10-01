def levenshtein(source, target):
    if source == '' or target == '':  # Base case handling
        return len(source) or len(target)

    elif source[0] == target[0]:
        return levenshtein(source[1:], target[1:])  # Corrected: Should be 0 + levenshtein(source[1:], target[1:])

    else:
        return 1 + min(
            levenshtein(source,     target[1:]),  # Cost for insertion
            levenshtein(source[1:], target[1:]),  # Cost for substitution
            levenshtein(source[1:], target)        # Cost for deletion
        )