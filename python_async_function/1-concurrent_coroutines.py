#!/usr/bin/env python3
"""Defines a function wait_n that takes in 2 int arguments (in this order) and returns a list of all the delays (float values) of the n calls to wait_random.
"""

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Run wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to run wait_random.
        max_delay (int): The maximum number of seconds to wait for each call.

    Returns:
        list[float]: A list of the actual delay times for each call.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
