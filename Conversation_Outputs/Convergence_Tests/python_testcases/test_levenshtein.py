import pytest
from load_testdata import load_json_testcases

def levenshtein(source, target):
    # Base case: if either string is empty, return the length of the other string
    # This represents the number of insertions needed to match the non-empty string
    if source == '' or target == '':
        return max(len(source), len(target))  # Using max for clarity

    # If the first characters match, no edit is needed; move to the next characters
    elif source[0] == target[0]:
        return levenshtein(source[1:], target[1:])  # Fixed: Do not add 1 when characters match

    # If the first characters do not match, consider all three possible edits
    else:
        return 1 + min(
            levenshtein(source,     target[1:]),  # Insertion
            levenshtein(source[1:], target[1:]),  # Substitution
            levenshtein(source[1:], target)       # Deletion
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
