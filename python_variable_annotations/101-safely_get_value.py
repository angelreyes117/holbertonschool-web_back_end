#!/usr/bin/env python3
"""Module containing the safely_get_value function."""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the value for a key in a mapping or a default value."""
    if key in dct:
        return dct[key]
    else:
        return default
