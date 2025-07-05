#!/usr/bin/env python3
"""Module for running multiple concurrent tasks."""
import asyncio
from typing import List
from .3_tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with specified max_delay and returns sorted delays.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for each task_wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Gather results as they complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert delay in correct position to maintain ascending order
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)
    
    return delays
