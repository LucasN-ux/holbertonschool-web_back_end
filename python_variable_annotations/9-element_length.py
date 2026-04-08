#!/usr/bin/env python3
"""Defines a function element_length that takes a list of sequences and returns a list of tuples with the length of each element in the list.
"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with the length of each element in a list.

    Args:
        lst: A list of sequences to be measured.

    Returns:
        A list of tuples with the length of each element in the list.
    """
    return [(i, len(i)) for i in lst]
