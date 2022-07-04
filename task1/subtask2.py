"""
Subtask 2.
"""
from utils.geometry import Rect


def task(r1: Rect, r2: Rect) -> bool:
    """
    :param r2:
    :param r1:
    :return:
    """
    return not (
        r1.top_right.x < r2.bottom_left.x or
        r1.bottom_left.x > r2.top_right.x or
        r1.top_right.y < r2.bottom_left.y or
        r1.bottom_left.y > r2.top_right.y
    )
