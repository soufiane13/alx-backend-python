#!/usr/bin/env python3

""" Async Comprehensions """

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine async_generator
    yield random number 0-10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
