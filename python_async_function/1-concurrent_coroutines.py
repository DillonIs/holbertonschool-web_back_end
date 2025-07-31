#!/usr/bin/env python3
"""Execute multiple async tasks at the same time"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Calls the function wait_random n amount of times"""

    delay = []
    times = []
    for x in range(n):
        times.append(wait_random(max_delay))

    for time in asyncio.as_completed(times):
        result = await time
        delay.append(result)

    return delay
