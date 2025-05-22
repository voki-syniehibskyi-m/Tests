import pytest
from calculator.calculator.basic_calc import BasicCalc

@pytest.fixture(scope="module")
def calculator():
    """Фикстура для создания экземпляра BasicCalc."""
    return BasicCalc()