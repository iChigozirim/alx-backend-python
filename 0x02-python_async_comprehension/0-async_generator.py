#!/usr/bin/env python3
"""Defines a coroutine called async_generator."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yeilds a random number between 0 and 10. Delays for a second"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
