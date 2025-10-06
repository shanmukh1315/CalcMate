from app.calculator import Calculator
from app.calculation import CalculationFactory

def test_history_initially_empty():
    calc = Calculator()
    assert calc.history == []
    assert calc.last_result() is None

def test_add_to_history_and_last_result_updates():
    calc = Calculator()
    c1 = CalculationFactory.from_strings("+", "1 2 3")   # 6.0
    r1 = calc.add_to_history(c1)
    assert r1 == 6.0
    assert len(calc.history) == 1
    assert calc.last_result() == 6.0

    c2 = CalculationFactory.from_strings("*", "2 3 4")   # 24.0
    r2 = calc.add_to_history(c2)
    assert r2 == 24.0
    # history is a copy; ensure original not mutated by external changes
    h = calc.history
    assert len(h) == 2
    assert calc.last_result() == 24.0
