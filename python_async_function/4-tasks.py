#!/usr/bin/env python3
"""Take the code from wait_n and alter it into task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls the function wait_random n amount of times"""

    tasks = [task_wait_random(max_delay) for i in range(n)]

    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
