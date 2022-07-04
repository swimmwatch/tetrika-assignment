"""
Subtask 1.
"""


def task(array: str) -> int:
    """
    Find index of first zero.
    :param array: String with 1 and 0
    :return: Index
    """
    try:
        res = array.index('0') - 1
    except ValueError:
        raise ValueError('0 not found')
    return res
