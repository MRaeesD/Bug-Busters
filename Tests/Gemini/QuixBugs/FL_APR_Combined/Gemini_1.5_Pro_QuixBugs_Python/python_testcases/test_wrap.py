import pytest
from load_testdata import load_json_testcases

def wrap(text, cols):
        lines = []
        while len(text) > cols:
            # Find the last space within the allowed column width
            end = text.rfind(' ', 0, cols) 
            if end == -1:
                end = cols
            # Exclude the space at 'end' from the next line
            line, text = text[:end], text[end + 1:] 
            lines.append(line)
        if text:  # Add any remaining text
            lines.append(text)
        return lines



testdata = load_json_testcases(wrap.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_wrap(input_data, expected):
    assert wrap(*input_data) == expected
