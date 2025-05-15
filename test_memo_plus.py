from calculator.calculator.basic_calc import CalcWithMemory
import pytest

def test_memo_plus():
    calc = CalcWithMemory()
    calc.memory = []
    result = calc.memo_plus(2)
    assert result == 2
    assert calc.memory == [2]

def test_negative_memo_plus():
    calc = CalcWithMemory()
    calc.memory = []
    with pytest.raises(ValueError, match="Сохранять можно только числа, получено"):
        calc.memo_plus('Some_string')