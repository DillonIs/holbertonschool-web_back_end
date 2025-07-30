#!/usr/bin/env python3
"""Duck typing task 9"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list"""
    return [(i, len(i)) for i in lst]
