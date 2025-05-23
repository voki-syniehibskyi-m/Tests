import pytest


@pytest.mark.critical
def test_add_with_memory(calculator_with_memory):
    result = calculator_with_memory.add(2)
    assert result == 12


def test_negative_add_with_memory(calculator_with_memory):
    calculator_with_memory.memo_minus()
    with pytest.raises(IndexError, match='Память пуста, нечего удалить из памяти или взять'):
        calculator_with_memory.add(4)

def test_add_with_memory_invalid(calculator_with_memory):
    result = calculator_with_memory.add("string")
    assert result == 10