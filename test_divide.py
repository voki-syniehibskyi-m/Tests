import pytest
from calculator.calculator.basic_calc import ZeroDivisionCatcher

@pytest.mark.critical
def test_divide_nums(calculator):
    result = calculator.divide(6, 2)
    assert result == 3

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionCatcher, match = 'На ноль делить не стоит, введите число > 0'):
        calculator.divide(5, 0)
