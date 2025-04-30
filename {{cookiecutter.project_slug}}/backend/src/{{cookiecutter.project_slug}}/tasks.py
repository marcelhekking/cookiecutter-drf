# Example file to illustrate how Celery tasks work.
# Every Django app can have a `tasks.py` file containing relevant tasks.

import random
from typing import List

from celery import shared_task


@shared_task
def add(x: int, y: int) -> int:
    return x + y


@shared_task(name="multiply_two_numbers")
def mul(x: int, y: int) -> int:
    total = x * (y * random.randint(3, 100))
    return total


@shared_task(name="sum_list_numbers")
def xsum(numbers: List[int]) -> int:
    return sum(numbers