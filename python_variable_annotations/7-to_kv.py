#!/usr/bin/env python3
"""Module containing the to_kv function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with a string and the square of an int or float."""
    return (k, v ** 2)
