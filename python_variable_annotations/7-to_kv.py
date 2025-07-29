#!/usr/bin/env python3
"""Type annotation function that takes a string k
and an int OR float v and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with string and float"""
    return (k, v * v)
