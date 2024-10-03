import pytest
from load_testdata import load_json_testcases

def levenshtein(source, target):
        if source == '' or target == '':
            return len(source) or len(target)

        elif source[0] == target[0]:
            # Bug fix: No need to add 1 here. Matching characters mean no edit.
            return levenshtein(source[1:], target[1:]) 

        else:
            # Bug fix: Add 1 to each recursive call to account for the edit.
            return 1 + min(
                levenshtein(source,     target[1:]), 
                levenshtein(source[1:], target[1:]), 
                levenshtein(source[1:], target)
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
