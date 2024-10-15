#!/usr/bin/env python3
"""
A module for asynchronous tasks using asyncio."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for `n` random amounts of time up to `max_delay` seconds.
    Returns a list of the wait times, sorted in ascending order.   
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): delay value to be passed to wait_random
    Returns:
        List[float]: list of ordered delays
    """
    resolves = await asyncio.gather(
        *(wait_random(max_delay) for i in range(n)))
    return sorted(resolves)
