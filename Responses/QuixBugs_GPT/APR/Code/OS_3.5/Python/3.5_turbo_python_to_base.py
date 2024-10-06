import string

def to_base(num, b):
    result = ''
    alphabet = string.digits + string.ascii_uppercase
    while num > 0:
        i = num % b
        num = num // b
        if i < len(alphabet):
            result = result + alphabet[i]
    return result
