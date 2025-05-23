import pytest
from calculator.calculator.basic_calc import CalcWithMemory, ZeroDivisionCatcher

@pytest.mark.critical
def test_divide_with_memory(calculator_with_memory):
    result = calculator_with_memory.divide(2)
    assert result == 0.2

def test_negative_divide_with_memory(calculator_with_memory):
    calculator_with_memory.memo_plus(0)
    with pytest.raises(ZeroDivisionCatcher):
        calculator_with_memory.divide(5)

