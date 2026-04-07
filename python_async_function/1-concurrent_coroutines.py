#!/usr/bin/env python3

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
    await asyncio.sleep(0)
    return await asyncio.gather(*tasks)
