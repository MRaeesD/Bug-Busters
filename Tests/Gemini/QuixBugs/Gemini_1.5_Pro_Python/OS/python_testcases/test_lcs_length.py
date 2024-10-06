import pytest
from load_testdata import load_json_testcases

def lcs_length(s, t):
    from collections import Counter

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i, j] = dp[i - 1, j - 1] + 1  # Consider both characters and previous substring length
            else:
                dp[i, j] = 0  # Reset if characters don't match

    return max(dp.values()) if dp else 0



testdata = load_json_testcases(lcs_length.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lcs_length(input_data, expected):
    assert lcs_length(*input_data) == expected
