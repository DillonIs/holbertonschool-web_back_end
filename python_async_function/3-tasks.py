#!/usr/bin/env python3
"""Non async function that returns async.task"""
import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an async task with specified max_delay"""
    return asyncio.Task(wait_random(max_delay))
