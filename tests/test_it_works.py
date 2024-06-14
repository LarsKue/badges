
import pytest

from badges import add_numbers


def test_add_numbers():
    assert add_numbers(2, 2) == 4


@pytest.mark.xfail
def test_fail():
    assert False


