#!/usr/bin/env python3
"""Module for creating asyncio Task from wait_random coroutine."""
import asyncio
from .0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio Task for wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for wait_random coroutine.

    Returns:
        asyncio.Task: Task object for wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
