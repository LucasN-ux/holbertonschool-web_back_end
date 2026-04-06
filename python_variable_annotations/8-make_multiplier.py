#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier: The float to multiply by.

    Returns:
        A function that multiplies a float by the given multiplier.
    """
    def multiplier_func(n: float) -> float:
        """Multiplies a float by the given multiplier.

        Args:
            n: The float to be multiplied.

        Returns:
            The result of multiplying the float by the given multiplier.
        """
        return n * multiplier

    return multiplier_func
