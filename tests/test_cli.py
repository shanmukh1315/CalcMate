import builtins
from typing import Iterator
from contextlib import contextmanager
from app.calculator import cli

@contextmanager
def feed_inputs(inputs: list[str]) -> Iterator[None]:
    itr = iter(inputs)
    original = builtins.input
    builtins.input = lambda prompt="": next(itr)
    try:
        yield
    finally:
        builtins.input = original

def run_cli_with(inputs: list[str]) -> str:
    from io import StringIO
    import sys
    saved = sys.stdout
    buf = StringIO()
    sys.stdout = buf
    try:
        with feed_inputs(inputs):
            cli.main()
    finally:
        sys.stdout = saved
    return buf.getvalue()

def test_cli_help_then_exit():
    out = run_cli_with(["help", "exit"])
    assert "CalcMate — Commands & Usage" in out
    assert "Goodbye!" in out

def test_cli_single_addition_flow():
    out = run_cli_with(["+", "1 2 3", "history", "exit"])
    assert "Result: 6.0" in out
    assert "add [1.0, 2.0, 3.0] = 6.0" in out

def test_cli_divide_by_zero():
    out = run_cli_with(["/", "1 0", "exit"])
    assert "Division by zero" in out

def test_cli_invalid_operation_then_exit():
    out = run_cli_with(["pow", "2 3", "exit"])
    assert "Unsupported operation" in out
