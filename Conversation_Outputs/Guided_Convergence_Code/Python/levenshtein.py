def levenshtein(source, target):
    if source == '' or target == '':
        return len(source) or len(target)

    elif source[0] == target[0]:
        # Bug fix: Removed the unnecessary '+ 1' as no edit is needed when characters match
        return levenshtein(source[1:], target[1:]) 

    else:
        return 1 + min(
            levenshtein(source,     target[1:]),
            levenshtein(source[1:], target[1:]),
            levenshtein(source[1:], target)
        )