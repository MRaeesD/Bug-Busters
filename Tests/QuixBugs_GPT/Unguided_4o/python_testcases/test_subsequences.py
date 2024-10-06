import pytest
from load_testdata import load_json_testcases

def subsequences(a, b, k):
        if k == 0:
            return [[]]  # Return a list of an empty list to allow recursion to return proper sublists

        ret = []
        for i in range(a, b + 1 - k + 1):  # Correct the loop to include the end range and ensure valid subsequences
            ret.extend(
                [[i] + rest for rest in subsequences(i + 1, b, k - 1)]
            )

        return ret


testdata = load_json_testcases(subsequences.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_subsequences(input_data, expected):
    assert subsequences(*input_data) == expected
