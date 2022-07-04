"""
Unittest for subtask №2.
"""
import pytest

from task1.subtask2 import task
from utils.geometry import Rect, Point2D


@pytest.mark.parametrize('r1,r2,expected', [
    (
        Rect(
            Point2D(1, 1),
            Point2D(2, 2)
        ),
        Rect(
            Point2D(3, 3),
            Point2D(4, 4)
        ),
        False
    )
])
def test_subtask2(r1: Rect, r2: Rect, expected: bool):
    actual = task(r1, r2)
    assert actual == expected
