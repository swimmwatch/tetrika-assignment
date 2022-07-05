"""
Unittests for task function.
"""
from typing import Optional

import pytest

from task3.solution import StudySessionData, overlap_study, \
    Interval, has_overlap, overlap


@pytest.mark.parametrize('i1,i2,expected', [
    (Interval(0, 0), Interval(0, 0), True),
    (Interval(0, 0), Interval(0, 1), True),
    (Interval(1, 2), Interval(0, 1), True),
    (Interval(1, 2), Interval(3, 4), False),
])
def test_has_overlap(i1: Interval, i2: Interval, expected: bool):
    actual = has_overlap(i1, i2)
    assert actual == expected


@pytest.mark.parametrize('i1,i2,expected', [
    (Interval(0, 0), Interval(0, 0), Interval(0, 0)),
    (Interval(0, 0), Interval(0, 1), Interval(0, 0)),
    (Interval(1, 2), Interval(0, 1), Interval(1, 1)),
    (Interval(1, 2), Interval(3, 4), None),
])
def test_overlap(i1: Interval, i2: Interval, expected: Optional[Interval]):
    actual = overlap(i1, i2)
    assert actual == expected


@pytest.mark.parametrize('start,end', [
    (0, -1),
    (1, 0),
])
def test_negative_interval(start: int, end: int):
    with pytest.raises(ValueError):
        Interval(start, end)


@pytest.mark.parametrize('data,expected', [
    (
        StudySessionData(
            tutor=[
                Interval(1594663290, 1594663430),
                Interval(1594663443, 1594666473)
            ],
            pupil=[
                Interval(1594663340, 1594663389),
                Interval(1594663390, 1594663395),
                Interval(1594663396, 1594666472)
            ],
            lesson=Interval(1594663200, 1594666800)
        ),
        3117
    ),
    (
        StudySessionData(
            tutor=[
                Interval(1594700035, 1594700364),
                Interval(1594702749, 1594705148),
                Interval(1594705149, 1594706463),
            ],
            pupil=[
                Interval(1594702789, 1594704500),
                Interval(1594702807, 1594704542),
                Interval(1594704512, 1594704513),
                Interval(1594704564, 1594705150),
                Interval(1594704581, 1594704582),
                Interval(1594704734, 1594705009),
                Interval(1594705095, 1594705096),
                Interval(1594705106, 1594706480),
                Interval(1594705158, 1594705773),
                Interval(1594705849, 1594706480),
                Interval(1594706500, 1594706875),
                Interval(1594706502, 1594706503),
                Interval(1594706524, 1594706524),
                Interval(1594706579, 1594706641),
            ],
            lesson=Interval(1594702800, 1594706400)
        ),
        3457
    ),
    (
        StudySessionData(
            tutor=[
                Interval(1594692017, 1594692066),
                Interval(1594692068, 1594696341)
            ],
            pupil=[
                Interval(1594692033, 1594696347),
            ],
            lesson=Interval(1594692000, 1594695600)
        ),
        3565
    ),
])
def test_task(data: StudySessionData, expected: int):
    actual = overlap_study(data)
    assert actual == expected
