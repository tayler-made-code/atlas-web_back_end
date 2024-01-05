#!/usr/bin/env python3

""" Take the code from wait_n and alter it into a new function
    task_wait_n. The code is nearly identical to wait_n except
    task_wait_random is being called """

import importlib
import asyncio
from typing import List
basic_async_syntax = importlib.import_module("0-basic_async_syntax")
wait_random = basic_async_syntax.wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Return list of delays in ascending order """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return sorted(delays)


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Wait for a random delay between 0 and max_delay """
    return asyncio.create_task(wait_random(max_delay))
