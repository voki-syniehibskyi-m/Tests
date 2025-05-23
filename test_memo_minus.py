import pytest

def test_memo_minus(calculator_with_memory):
    result = calculator_with_memory.memo_minus()
    assert result == 10, "Память инициируется как 10"
    assert calculator_with_memory.memory == []

def test_negative_memo_minus(calculator_with_memory):
    calculator_with_memory.memo_minus()
    with pytest.raises(IndexError, match='Память пуста, нечего удалить из памяти или взять'):
        calculator_with_memory.memo_minus()