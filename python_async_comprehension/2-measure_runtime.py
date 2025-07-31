#!/usr/bin/env python3
"""Measuring parallel runtime"""
import asyncio
import time
import random
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the total runtime of multiple executions"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
