#!/usr/bin/env python3
"""Module that measures the total runtime of async coroutine functions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of the 4 async_comprehension coroutines
    when executed concurrently.

    Returns:
        float: Total runtime in seconds.
    """
    tasks = []

    start = time.time()

    for num in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))

    await asyncio.gather(*tasks)

    end = time.time()

    return end - start
