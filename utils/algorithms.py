"""
Some algorithms utils.
"""
from typing import Callable, Iterable, TypeVar, Optional

T = TypeVar('T')


def find_first(
        condition: Callable[[T], bool],
        collection: Iterable[T]
) -> Optional[T]:
    """
    Find first element by condition result.

    :param condition: Predicate
    :param collection: Some
    :return: Element
    """
    for el in collection:
        if condition(el):
            return el
    else:
        return None
