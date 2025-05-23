import pytest


@pytest.mark.xfail
@pytest.mark.critical
def test_subtract_with_memory(calculator_with_memory):
    result = calculator_with_memory.subtract(5)
    assert result == 5


def test_negative_subtract_with_memory(calculator_with_memory):
    calculator_with_memory.memo_minus()
    with pytest.raises(IndexError, match="Память пуста, нечего удалить из памяти или взять"):
        calculator_with_memory.subtract(10)

def test_subtract_with_memory_invalid(calculator_with_memory):
    result = calculator_with_memory.subtract("string")
    assert result == -9

