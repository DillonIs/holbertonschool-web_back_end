#!/usr/bin/env python3
"""Type annotated function that multiplies a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function multiplying a float by multiplier"""
    def result(value: float) -> float:
        """Returns float multiplied by multiplier"""
        return value * multiplier
    return result
