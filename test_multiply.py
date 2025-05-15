import pytest
from calculator.calculator.basic_calc import BasicCalc

@pytest.mark.critical
def test_multiply_nums():
    calc = BasicCalc()
    result = calc.multiply(5, 5)
    assert result == 25

def test_negative_multiply_nums():
    calc = BasicCalc()
    result = calc.multiply(5, 'string')
    assert result == 0



