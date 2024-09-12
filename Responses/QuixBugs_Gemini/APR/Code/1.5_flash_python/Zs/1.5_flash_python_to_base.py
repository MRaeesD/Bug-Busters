import string
def to_base(num, b):
    result = ''
    alphabet = string.digits + string.ascii_uppercase
    while num > 0:
        i = num % b
        num = num // b
        # Change: append the digit at the beginning of the result string
        result = alphabet[i] + result 
    return result
