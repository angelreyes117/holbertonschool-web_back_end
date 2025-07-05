#!/usr/bin/env python3
"""Module for measuring runtime of concurrent coroutines."""
import asyncio
import time
from .1_concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures total execution time for wait_n(n, max_delay) and returns average.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        float: Average time per call (total_time / n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
