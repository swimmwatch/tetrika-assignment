"""
Unittest for subtask №2.
"""
from typing import Optional

import pytest

from task1.subtask2 import Rect
from task1.subtask3 import task
from utils.geometry import Point2D


@pytest.mark.parametrize('r1,r2,expected', [
    (
        Rect(
            Point2D(3, 3),
            Point2D(5, 5)
        ),
        Rect(
            Point2D(1, 1),
            Point2D(4, 3.5)
        ),
        0.5
    )
])
def test_subtask3(r1: Rect, r2: Rect, expected: Optional[float]):
    actual = task(r1, r2)
    assert actual == expected
