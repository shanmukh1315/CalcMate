from __future__ import annotations
from typing import Iterable
Number = float | int

def add(numbers: Iterable[Number]) -> float:
    total = 0.0
    for n in numbers:
        total += float(n)
    return total

def subtract(numbers: Iterable[Number]) -> float:
    nums = [float(n) for n in numbers]
    if not nums:
        return 0.0
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result

def multiply(numbers: Iterable[Number]) -> float:
    result = 1.0
    for n in numbers:
        result *= float(n)
    return result

def divide(numbers: Iterable[Number]) -> float:
    nums = [float(n) for n in numbers]
    if not nums:
        return 0.0
    result = nums[0]
    for n in nums[1:]:
        try:
            result /= n
        except ZeroDivisionError as exc:
            raise exc
    return result
