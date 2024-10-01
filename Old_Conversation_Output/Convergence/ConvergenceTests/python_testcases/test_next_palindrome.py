import pytest
from load_testdata import load_json_testcases

def next_palindrome(digit_list):
    high_mid = len(digit_list) // 2
    low_mid = (len(digit_list) - 1) // 2
    
    while high_mid < len(digit_list) and low_mid >= 0:
        if digit_list[high_mid] == 9:  # Handles carry for 9s
            digit_list[high_mid] = 0
            digit_list[low_mid] = 0
            high_mid += 1  # Move right
            low_mid -= 1   # Move left
        else:
            digit_list[high_mid] += 1
            if low_mid != high_mid:
                digit_list[low_mid] += 1
            break  # Continue processing other digits
    
    if high_mid == len(digit_list):  # All digits were 9
        return [1] + (len(digit_list)) * [0] + [1]
    
    # Ensure the palindrome property is maintained for the rest of the digits
    for i in range((len(digit_list) + 1) // 2):
        digit_list[-(i+1)] = digit_list[i]
    
    return digit_list


testdata = load_json_testcases(next_palindrome.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_next_palindrome(input_data, expected):
    assert next_palindrome(*input_data) == expected
