#!/usr/bin/env python3
"""Module containing the zoom_array function."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list with each item in the tuple repeated by factor."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
