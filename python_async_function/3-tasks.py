#!/usr/bin/env python3
"""Defines task_wait_random that returns an asyncio.Task."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio.Task for wait_random.

    Args:
        max_delay (int): The maximum delay passed to wait_random.

    Returns:
        asyncio.Task: The task running wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
