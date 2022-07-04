"""
Geometry utils.
"""
from dataclasses import dataclass
from typing import NamedTuple


class Point2D(NamedTuple):
    x: float
    y: float


@dataclass
class Rect:
    bottom_left: Point2D
    top_right: Point2D

    def _validate(self):
        return self.bottom_left.x <= self.top_right.x and \
               self.bottom_left.y <= self.top_right.y

    def __post_init__(self):
        if not self._validate():
            raise ValueError(
                'Bottom left point must be to the left'
                ' and bottom than top right point'
            )
