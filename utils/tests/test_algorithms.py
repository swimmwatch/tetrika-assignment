"""
Unittests for algorithms utils.
"""
from typing import TypeVar, Iterable, Optional, Callable

import pytest

from utils.algorithms import find_first

T = TypeVar('T')


def dummy_predicate(val: bool = True) -> Callable[[T], bool]:
    return lambda x: val


@pytest.mark.parametrize('condition,collection,expected', [
    (dummy_predicate(), [], None),
    (dummy_predicate(), [1], 1),
    (dummy_predicate(), [1, 2], 1),
    (dummy_predicate(False), [1], None),
    (lambda x: x == 2, [1, 2, 3], 2)
])
def test_find_first(
        condition: Callable[[T], bool],
        collection: Iterable[T],
        expected: Optional[T]
):
    actual = find_first(condition, collection)
    assert actual == expected
