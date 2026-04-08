#!/usr/bin/env python3
"""Defines a function to_kv that takes a string k and an int or float v and returns a tuple.
"""


def to_kv(k: str, v: int | float) -> tuple:
    """Returns a tuple of the key and value.

    Args:
        k: The key to be used in the tuple.
        v: The value to be used in the tuple.
    Returns:
        A tuple of the key and value.
    """
    return (k, v * v)
