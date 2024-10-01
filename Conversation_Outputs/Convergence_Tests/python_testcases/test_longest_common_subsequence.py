import pytest
from load_testdata import load_json_testcases

def longest_common_subsequence(a, b):
    if not a or not b:
        return ''

    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])  # bug fixed: advance both strings

    else:
        return max(
            longest_common_subsequence(a, b[1:]),
            longest_common_subsequence(a[1:], b),
            key=len
        )


testdata = load_json_testcases(longest_common_subsequence.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_longest_common_subsequence(input_data, expected):
    assert longest_common_subsequence(*input_data) == expected
