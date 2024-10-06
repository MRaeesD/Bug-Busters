import pytest
from load_testdata import load_json_testcases

def lcs_length(s, t):
    from collections import defaultdict

    dp = defaultdict(int)
    max_length = 0

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    dp[i, j] = 1
                else:
                    dp[i, j] = dp[i - 1, j - 1] + 1
                max_length = max(max_length, dp[i, j])

    return max_length


testdata = load_json_testcases(lcs_length.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lcs_length(input_data, expected):
    assert lcs_length(*input_data) == expected
