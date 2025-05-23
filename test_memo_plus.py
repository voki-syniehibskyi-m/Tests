import pytest

def test_memo_plus(calculator_with_memory):
    calculator_with_memory.memo_plus(20)
    assert calculator_with_memory.last_value == 20

def test_negative_memo_plus(calculator_with_memory):
    with pytest.raises(ValueError, match="Сохранять можно только числа, получено"):
        calculator_with_memory.memo_plus('Some_string')

