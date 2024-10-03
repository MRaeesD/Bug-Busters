import pytest
from load_testdata import load_json_testcases

def lcs_length(s, t):
        from collections import Counter

        dp = Counter()

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    # Fix: Check if we're at the beginning of either string. 
                    # If not, add 1 to the diagonal element representing the previous match in both strings.
                    dp[i, j] = 1 if i == 0 or j == 0 else dp[i - 1, j - 1] + 1 
                else:
                    # Fix: If characters don't match, the length of LCS at this point is 0
                    dp[i, j] = 0 

        return max(dp.values()) if dp else 0


testdata = load_json_testcases(lcs_length.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lcs_length(input_data, expected):
    assert lcs_length(*input_data) == expected
