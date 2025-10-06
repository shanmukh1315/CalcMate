import pytest
from app.calculation import CalculationFactory

@pytest.mark.parametrize("op, nums, expected", [
    ("+", "1 2 3.5", 6.5),
    ("add", "1 2", 3.0),
    ("-", "5 2 1", 2.0),
    ("multiply", "2 3 4", 24.0),
    ("/", "8 2", 4.0),
])
def test_factory_and_compute(op, nums, expected):
    c = CalculationFactory.from_strings(op, nums)
    assert c.compute() == pytest.approx(expected)

def test_factory_invalid_op():
    with pytest.raises(ValueError):
        CalculationFactory.from_strings("power", "2 3")

def test_factory_bad_number():
    with pytest.raises(ValueError):
        CalculationFactory.from_strings("+", "2 x")

def test_factory_divide_zero():
    with pytest.raises(ZeroDivisionError):
        c = CalculationFactory.from_strings("/", "1 0")
        c.compute()
