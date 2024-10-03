import string
def to_base(num, b):
        result = ''
        alphabet = string.digits + string.ascii_uppercase
        while num > 0:
            i = num % b
            num = num // b
            # Prepend the new digit to the beginning of the result string
            result =  alphabet[i] + result # this line is fixed
        return result
