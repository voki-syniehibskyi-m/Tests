import pytest

from calculator.calculator.basic_calc import CalcWithMemory

def test_last_value():
    calc = CalcWithMemory()
    calc.memory = [1,2,3]
    assert calc.last_value == 3

def test_negative_last_value():
    calc = CalcWithMemory()
    calc.memory = []
    with pytest.raises(IndexError):
        calc.last_value()
