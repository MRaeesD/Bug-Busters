import pytest
from load_testdata import load_json_testcases

def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        for c in range(r + 1):  # Iterate from 0 to r (inclusive)
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0  # Corrected off-by-one error
            row.append(upleft + upright)
        rows.append(row)
    
    return rows


testdata = load_json_testcases(pascal.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_pascal(input_data, expected):
    assert pascal(*input_data) == expected
