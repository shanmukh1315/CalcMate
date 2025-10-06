import pytest
from app.operation import add, subtract, multiply, divide

@pytest.mark.parametrize("nums, expected", [
    ([], 0.0), ([1], 1.0), ([1, 2, 3.5], 6.5),
])
def test_add(nums, expected):
    assert add(nums) == pytest.approx(expected)

@pytest.mark.parametrize("nums, expected", [
    ([], 0.0), ([5], 5.0), ([5, 2], 3.0), ([10, 2, 3], 5.0),
])
def test_subtract(nums, expected):
    assert subtract(nums) == pytest.approx(expected)

@pytest.mark.parametrize("nums, expected", [
    ([], 1.0), ([3], 3.0), ([2, 3, 4], 24.0), ([2, 0.5], 1.0),
])
def test_multiply(nums, expected):
    assert multiply(nums) == pytest.approx(expected)

def test_divide_basic():
    assert divide([8, 2]) == 4.0
    assert divide([9, 3, 3]) == 1.0

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide([1, 0])
