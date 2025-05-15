import pytest
from calculator.calculator.basic_calc import CalcWithMemory

@pytest.mark.critical
def test_add_with_memory():
    calc = CalcWithMemory()
    calc.memory = []
    calc.memo_plus(2)
    result = calc.add(2)
    assert result == 4
    assert calc.memory == [4]

def test_negative_add_with_memory():
    calc = CalcWithMemory()
    calc.memory = []
    with pytest.raises(IndexError, match='Память пуста, нечего удалить из памяти или взять'):
        calc.add(4)

def test_add_with_memory_invalid():
    calc = CalcWithMemory()
    calc.memory = [3]
    result = calc.add("string")
    assert result == 3
    assert calc.memory == [3]