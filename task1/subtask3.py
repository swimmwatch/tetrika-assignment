"""
Subtask 2.
"""
from typing import Optional

from task1 import subtask2
from utils.geometry import Rect


def task(r1: Rect, r2: Rect) -> Optional[float]:
    """
    Find intersection square of two rectangles.

    :param r1: First rectangle
    :param r2: Second rectangle
    :return: Intersection square
    """
    if not subtask2.task(r1, r2):
        return None

    dx = min(r1.top_right.x, r2.top_right.x) - \
        max(r1.bottom_left.x, r2.bottom_left.x)
    dy = min(r1.top_right.y, r2.top_right.y) - \
        max(r1.bottom_left.y, r2.bottom_left.y)

    return dx * dy
