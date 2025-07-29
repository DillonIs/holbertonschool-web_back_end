#!/usr/bin/env python3
"""Type annotation the sum of mixed lists"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of a mixed list of integers and floats"""
    return sum(mxd_list)
