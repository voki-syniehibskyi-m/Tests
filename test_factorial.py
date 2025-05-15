import pytest
from calculator.calculator.factorial_timer import factorial

def test_factorial():
    assert factorial(5) == 120, "5! должно быть 120"

def test_negative_factorial():
    with pytest.raises(ValueError, match="Факториал не определён для отрицательных чисел"):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial("string")