#!/usr/bin/env python3
"""Take the code from wait_n and alter it into task_wait_n"""
import asyncio
from typing import List
from bisect import insort

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Calls the function wait_random n amount of times"""

    delays = []
    tasks = [task_wait_random(max_delay) for i in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        insort(delays, delay)

    return delay
