"""
Unittests for subtask №1.
"""
import pytest

from task1.subtask1 import task


@pytest.mark.parametrize('array,expected', [
    ('10', 0),
    ('110', 1),
    ('111111111110000000000000000', 10)
])
def test_subtask1(array: str, expected: int):
    actual = task(array)
    assert actual == expected
