"""
Some algorithms utils.
"""
from itertools import zip_longest
from typing import Callable, Iterable, TypeVar, Optional, Any, Tuple

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


def batch(
        iterable: Iterable[T],
        n: int,
        fillvalue: Any = None
) -> Iterable[Tuple[T]]:
    """Collect data into fixed-length chunks or blocks"""
    iters = [iter(iterable)] * n
    return zip_longest(*iters, fillvalue=fillvalue)
