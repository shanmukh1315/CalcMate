from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Iterable, Tuple
from app.operation import add, subtract, multiply, divide

OperationFunc = Callable[[Iterable[float]], float]
OP_MAP: dict[str, OperationFunc] = {
    "+": add, "add": add, "addition": add,
    "-": subtract, "sub": subtract, "subtract": subtract,
    "*": multiply, "mul": multiply, "multiply": multiply,
    "/": divide, "div": divide, "divide": divide,
}

@dataclass(frozen=True)
class Calculation:
    operands: Tuple[float, ...]
    operation: OperationFunc
    def compute(self) -> float:
        return self.operation(self.operands)

class CalculationFactory:
    @staticmethod
    def from_strings(op: str, raw_numbers: str) -> Calculation:
        key = (op or "").strip().lower()
        if key not in OP_MAP:
            raise ValueError(f"Unsupported operation: {op!r}")
        operands: list[float] = []
        for token in (raw_numbers or "").split():
            try:
                operands.append(float(token))
            except ValueError as exc:
                raise ValueError(f"Invalid number: {token!r}") from exc
        return Calculation(tuple(operands), OP_MAP[key])
