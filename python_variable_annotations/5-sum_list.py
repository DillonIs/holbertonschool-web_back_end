#!/usr/bin/env python3
"""Type annotated function that takes a list of floats
returns the sum of the list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
