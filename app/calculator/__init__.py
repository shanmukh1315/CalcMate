from __future__ import annotations
from typing import List
from app.calculation import Calculation

class Calculator:
    def __init__(self) -> None:
        self._history: List[Calculation] = []
    @property
    def history(self) -> list[Calculation]:
        return list(self._history)
    def add_to_history(self, calc: Calculation) -> float:
        result = calc.compute()
        self._history.append(calc)
        return result
    def last_result(self) -> float | None:
        if not self._history:
            return None
        return self._history[-1].compute()
