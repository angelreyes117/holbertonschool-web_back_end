#!/usr/bin/env python3
"""Module containing the safe_first_element function."""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of a sequence or None if empty."""
    if lst:
        return lst[0]
    else:
        return None
