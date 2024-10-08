import pytest
from load_testdata import load_json_testcases

def flatten(arr):
    for x in arr:
        if isinstance(x, list):
            for y in flatten(x):
                yield y
        else:
            yield x  # Fix: Directly yield the non-list object instead of calling flatten on a non-list object

testdata = load_json_testcases(flatten.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_flatten(input_data, expected):
    assert list(flatten(*input_data)) == expected
