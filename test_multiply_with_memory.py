import pytest
from calculator.calculator.basic_calc import CalcWithMemory

@pytest.mark.critical
def test_multiply_with_memory():
    calc = CalcWithMemory()
    calc.memory = [2]
    result = calc.multiply(5)
    assert result == 10
    assert calc.memory == [10]

def test_negative_multiply_with_memory():
    calc = CalcWithMemory()
    calc.memory = []
    with pytest.raises(IndexError, match='Память пуста, нечего удалить из памяти или взять'):
        calc.multiply(6)

