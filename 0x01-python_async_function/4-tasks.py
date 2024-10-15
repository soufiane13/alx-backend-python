#!/usr/bin/env python3
""" A module for creating and running multiple asyncio Tasks concurrently."""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Return the wait_random n times."""
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    return sorted(wait_times)
