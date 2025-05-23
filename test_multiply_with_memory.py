import pytest

@pytest.mark.critical
def test_multiply_with_memory(calculator_with_memory):
    result = calculator_with_memory.multiply(5)
    assert result == 50

def test_negative_multiply_with_memory(calculator_with_memory):
    calculator_with_memory.memo_minus()
    with pytest.raises(IndexError, match='Память пуста, нечего удалить из памяти или взять'):
        calculator_with_memory.multiply(6)

