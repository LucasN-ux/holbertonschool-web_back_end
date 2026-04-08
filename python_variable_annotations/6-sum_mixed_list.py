#!/usr/bin/env python3
"""Defines a function sum_mixed_list that takes a list of integers and floats
and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats.

    Args:
        mxd_lst: A list of integers and floats to be summed.

    Returns:
        The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
