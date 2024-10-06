def next_palindrome(digit_list):
    n = len(digit_list)
    if n == 1:
        if digit_list[0] == 9:
            return [1, 0, 1]
        else:
            return [digit_list[0] + 1]

    left_part = digit_list[:(n // 2)]
    if n % 2 == 0:
        middle_part = []
    else:
        middle_part = [digit_list[n // 2]]
    reversed_left_part = left_part[::-1]
    
    new_palindrome = left_part + middle_part + reversed_left_part
    
    if new_palindrome > digit_list:
        return new_palindrome
    
    carry = 1
    if n % 2 == 1:
        middle_part[0] += carry
        carry = 0
        if middle_part[0] > 9:
            middle_part[0] = 0
            carry = 1
    
    i = len(left_part) - 1
    while carry > 0 and i >= 0:
        left_part[i] += carry
        carry = 0
        if left_part[i] > 9:
            left_part[i] = 0
            carry = 1
        i -= 1
    
    if carry > 0:
        left_part = [1] + left_part
        if n % 2 == 0:
            return left_part + left_part[::-1]
        else:
            return left_part + [0] + left_part[::-1]
    
    reversed_left_part = left_part[::-1]
    if n % 2 == 0:
        return left_part + reversed_left_part
    else:
        return left_part + middle_part + reversed_left_part