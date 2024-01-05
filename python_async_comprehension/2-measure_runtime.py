#!/usr/bin/env python3

""" Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather

    measure_runtime should measure the total runtime and return it

    Notice that the total runtime is roughly 10 seconds,
    explain it to yourself:
    
    Sleep in 0-async_generator.py is 1 second causing the total runtime
    to be 10 seconds and some change """

import asyncio
import time
from typing import Generator, List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure runtime """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start
