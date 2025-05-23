import pytest


def test_last_value(calculator_with_memory):
    assert calculator_with_memory.last_value == 10, "Инициирован как 10"

def test_negative_last_value(calculator_with_memory):
    calculator_with_memory.memory = []
    with pytest.raises(IndexError):
        calculator_with_memory.last_value()
