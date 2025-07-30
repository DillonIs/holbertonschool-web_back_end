#!/usr/bin/env python3
"""Aysnc that takes an integer argument and
waits a random delay between 0 and max_delay"""
from random import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits a random delay up to a specified maximum"""
    delay = random() * max_delay

    await asyncio.sleep(delay)

    return delay
