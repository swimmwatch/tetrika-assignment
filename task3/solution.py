"""
Solution for task №3.
"""
from dataclasses import dataclass
from itertools import tee, combinations, product
from pprint import pprint
from typing import List, Optional


@dataclass
class Interval:
    """
    Timestamp interval.
    """
    start: int
    end: int

    def _validate(self) -> bool:
        return self.start <= self.end

    def __post_init__(self):
        if not self._validate():
            raise ValueError('start must be less than end')

    def __hash__(self):
        return hash((self.start, self.end))


@dataclass
class StudySessionData:
    lesson: Interval
    pupil: List[Interval]
    tutor: List[Interval]


def has_overlap(i1: Interval, i2: Interval) -> bool:
    """
    Check overlap between two intervals.

    :param i1: First interval
    :param i2: Second interval
    """
    latest_start = max(i1.start, i2.start)
    earliest_end = min(i1.end, i2.end)
    return latest_start <= earliest_end


def overlap(i1: Interval, i2: Interval) -> Optional[Interval]:
    """
    Find intersection between two intervals.

    :param i1: First interval
    :param i2: Second interval
    :return:
    """
    if not has_overlap(i1, i2):
        return None

    return Interval(
        max(i1.start, i2.start),
        min(i1.end, i2.end)
    )


def overlap_study(data: StudySessionData) -> int:
    # intersection between lesson and tutor
    tutor = set(data.tutor)
    lesson_and_tutor = filter(
        None,
        (overlap(data.lesson, i) for i in tutor)
    )
    # intersection with pupil
    pupil = set(data.pupil)
    curr_and_pupil = list(filter(
        None,
        (
            overlap(i, j)
            for i in lesson_and_tutor
            for j in pupil
        )
    ))
    # find intersections between self
    intersections = set(curr_and_pupil)
    res = []
    for i in intersections:
        new_i = i
        for j in intersections:
            if has_overlap(new_i, j):
                new_i = overlap(new_i, j)
        res.append(new_i)

    return sum(i.end - i.start for i in res)
