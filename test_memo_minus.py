import pytest
from calculator.calculator.basic_calc import CalcWithMemory

def test_memo_minus():
    calc = CalcWithMemory()
    calc.memory = [5]
    result = calc.memo_minus()
    assert result == 5
    assert calc.memory == []

def test_negative_memo_minus():
    calc = CalcWithMemory()
    calc.memory = []
    with pytest.raises(IndexError, match='Память пуста, нечего удалить из памяти или взять'):
        calc.memo_minus()