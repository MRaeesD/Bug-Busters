import pytest
from load_testdata import load_json_testcases

def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols  # Potential infinite loop if no space is found
        else:
            # Adjust end to avoid losing trailing spaces in the next iteration
            while end < len(text) and text[end] == ' ':
                end += 1
        line, text = text[:end], text[end:]  # Potential space preservation issue
        lines.append(line)
    
    # Append the last segment of the text
    if text:
        lines.append(text)  # Missing logic to append the last segment of the text

    return lines


testdata = load_json_testcases(wrap.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_wrap(input_data, expected):
    assert wrap(*input_data) == expected
