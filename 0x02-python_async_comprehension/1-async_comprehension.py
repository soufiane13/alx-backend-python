#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function that collects 10 random numbers using an async comprehension.

    Returns:
        List[float]: A list of 10 random float numbers between 0 and 10.
    """
    a = [i async for i in async_generator()]
    return a
