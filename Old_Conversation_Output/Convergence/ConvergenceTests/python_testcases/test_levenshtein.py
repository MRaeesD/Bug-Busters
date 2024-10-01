import pytest
from load_testdata import load_json_testcases

def levenshtein(source, target):
    if source == '' or target == '':  # Base case handling
        return len(source) or len(target)

    elif source[0] == target[0]:
        return levenshtein(source[1:], target[1:])  # Corrected: Should be 0 + levenshtein(source[1:], target[1:])

    else:
        return 1 + min(
            levenshtein(source,     target[1:]),  # Cost for insertion
            levenshtein(source[1:], target[1:]),  # Cost for substitution
            levenshtein(source[1:], target)        # Cost for deletion
        )


testdata = load_json_testcases(levenshtein.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_levenshtein(input_data, expected):
    if input_data == [
        "amanaplanacanalpanama",
        "docnoteidissentafastneverpreventsafatnessidietoncod",
    ]:
        pytest.skip("Takes too long to pass!")

    assert levenshtein(*input_data) == expected
