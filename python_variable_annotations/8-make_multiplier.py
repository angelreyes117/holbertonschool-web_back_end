#!/usr/bin/env python3
"""Module containing the make_multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiplier_function(x: float) -> float:
        """Multiplies a float by the outer function's multiplier."""
        return x * multiplier
    return multiplier_function
