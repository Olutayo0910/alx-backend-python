#!/usr/bin/env python3
"""Defines basic asynchronous syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous syntax"""
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
