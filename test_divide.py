import pytest

from calculator.calculator.basic_calc import BasicCalc, ZeroDivisionCatcher
from calculator.calculator.factorial_timer import cached_factorial


@pytest.mark.critical
def test_divide_nums():
    calc = BasicCalc()
    result = calc.divide(6, 2)
    assert result == 3

def test_divide_by_zero():
    calc = BasicCalc()
    with pytest.raises(ZeroDivisionCatcher, match = 'На ноль делить не стоит, введите число > 0'):
        calc.divide(5, 0)
