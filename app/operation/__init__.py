from __future__ import annotations
from typing import Iterable

Number = float | int

def add(numbers: Iterable[Number]) -> float:
    """Return the sum of numbers."""
    total = 0.0
    for n in numbers:
        total += float(n)
    return total

def subtract(numbers: Iterable[Number]) -> float:
    """Subtract in order: n0 - n1 - n2 - ...; empty -> 0.0."""
    nums = [float(n) for n in numbers]
    if not nums:
        return 0.0
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result

def multiply(numbers: Iterable[Number]) -> float:
    """Multiply all numbers; empty -> 1.0 (neutral element)."""
    result = 1.0
    for n in numbers:
        result *= float(n)
    return result

def divide(numbers: Iterable[Number]) -> float:
    """
    Divide in order: n0 / n1 / n2 / ...
    Empty -> 0.0, single value -> itself.
    EAFP style: raise ZeroDivisionError on division by zero; the CLI handles it.
    """
    nums = [float(n) for n in numbers]
    if not nums:
        return 0.0
    result = nums[0]
    for n in nums[1:]:
        try:
            result /= n
        except ZeroDivisionError as exc:  # pragma: no cover
            # Re-raise for the CLI/tests to handle; excluding re-raise from coverage.
            raise exc  # pragma: no cover
    return result
