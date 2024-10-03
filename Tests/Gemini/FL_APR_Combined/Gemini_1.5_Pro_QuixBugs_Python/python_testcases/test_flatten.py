import pytest
from load_testdata import load_json_testcases

def flatten(arr):
        for x in arr:
            if isinstance(x, list):
                for y in flatten(x):
                    yield y
            else:
                yield x # Fixed: Removed the erroneous call to 'flatten(x)' and replaced it with 'yield x' to yield the non-list element directly.



testdata = load_json_testcases(flatten.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_flatten(input_data, expected):
    assert list(flatten(*input_data)) == expected
