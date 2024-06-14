
import pytest


@pytest.mark.add
def test_add_numbers():
    from badges import add_numbers
    assert add_numbers(2, 2) == 4


@pytest.mark.subtract
def test_subtract_numbers():
    from badges import subtract_numbers
    assert subtract_numbers(2, 2) == 0
