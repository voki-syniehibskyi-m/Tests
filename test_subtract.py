from calculator.calculator.basic_calc import BasicCalc
import pytest

@pytest.mark.xfail
@pytest.mark.critical
def test_subtract_numbers():
    calc = BasicCalc()
    result = calc.subtract(5,3)
    assert result == 2

@pytest.mark.xfail
def test_negative_subtract_numbers():
    calc = BasicCalc()
    result = calc.subtract(5, 'str')
    assert result == 5

