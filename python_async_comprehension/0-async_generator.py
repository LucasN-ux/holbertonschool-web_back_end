#!/usr/bin/env python3
"""Defines async_generator coroutine."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait 1 second, then yield a random float between 0-10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
