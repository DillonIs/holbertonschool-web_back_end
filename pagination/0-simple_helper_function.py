#!/usr/bin/env python3
"""Simple helper function named index_range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Helper function that takes two integers and returns a Tuple
    with a start index and an end index"""

    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
