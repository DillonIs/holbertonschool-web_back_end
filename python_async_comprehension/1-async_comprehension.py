#!/usr/bin/env python3
"""Async Comprehension"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension
    over async_generator then returns the 10 random numbers"""
    return [value async for value in async_generator()]
