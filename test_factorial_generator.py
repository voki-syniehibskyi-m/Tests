import pytest
from calculator.calculator.factorial_timer import factorial_generator

def test_factorial_generator():
    gen = factorial_generator(5)
    expected = [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]
    result = list(gen)
    assert result == expected, "Генератор должен выдать правильные факториалы"

import pytest
from calculator.calculator.factorial_timer import factorial_generator

def test_negative_factorial_generator():
    with pytest.raises(ValueError, match="Максимальное число не может быть отрицательным"):
        list(factorial_generator(-1))
    with pytest.raises(TypeError):
        list(factorial_generator("string"))