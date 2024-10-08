import pytest
from load_testdata import load_json_testcases

def lcs_length(s, t):
    from collections import Counter

    dp = Counter()

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:  # compare s[i-1] and t[j-1]
                dp[i, j] = dp[i - 1, j - 1] + 1  # use dp[i-1, j-1] for the previous diagonal value
            else:
                dp[i, j] = 0  # reset to 0 if characters do not match

    return max(dp.values()) if dp else 0


testdata = load_json_testcases(lcs_length.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lcs_length(input_data, expected):
    assert lcs_length(*input_data) == expected
