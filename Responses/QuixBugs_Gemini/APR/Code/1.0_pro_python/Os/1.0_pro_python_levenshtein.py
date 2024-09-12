return 1 + min(
            levenshtein(source,     target[1:]),
            levenshtein(source[1:], target),  # Corrected the second call
            levenshtein(source[1:], target)
        )
