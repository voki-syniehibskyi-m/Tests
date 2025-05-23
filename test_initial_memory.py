import pytest

def test_initial_memory(calculator_with_memory):
    assert calculator_with_memory.last_value == 10

