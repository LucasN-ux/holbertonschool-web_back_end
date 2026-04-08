#!/usr/bin/env python3
"""Defines an asynchronous coroutine wait_random that takes in an integer
max_delay and waits for a random delay between 0 and max_delay seconds and
eventually returns the delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay (inclusive) seconds.

    Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
