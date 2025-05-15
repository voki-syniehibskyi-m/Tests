import pytest
from calculator.calculator.basic_calc import CalcWithMemory

@pytest.mark.xfail
@pytest.mark.critical
def test_subtract_with_memory():
    calc = CalcWithMemory()
    calc.memory = [10]
    result = calc.subtract(5)
    assert result == -5
    assert calc.memory == [-5]

def test_negative_subtract_with_memory():
    calc = CalcWithMemory()
    calc.memory = []
    with pytest.raises(IndexError, match="Память пуста, нечего удалить из памяти или взять"):
        calc.subtract(10)

def test_subtract_with_memory_invalid():
    calc = CalcWithMemory()
    calc.memory = [5]
    result = calc.subtract("string")
    assert result == -5
    assert calc.memory == [-5]
