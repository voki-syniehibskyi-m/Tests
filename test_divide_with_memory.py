import pytest
from calculator.calculator.basic_calc import CalcWithMemory, ZeroDivisionCatcher

@pytest.mark.critical
def test_divide_with_memory():
    calc = CalcWithMemory()
    calc.memory = [1,3,4]
    result = calc.divide(12)
    assert result == 3

def test_negative_divide_with_memory():
    calc = CalcWithMemory()
    calc.memory = [1,2,0]
    with pytest.raises(ZeroDivisionCatcher):
        calc.divide(5)

