import pytest
from calculator.calculator.basic_calc import BasicCalc, CalcWithMemory
import os

@pytest.fixture(scope="function")
def calculator(tmp_path):
    """Фикстура для создания экземпляра BasicCalc."""
    calc = BasicCalc()
    calc.log_file = tmp_path / "calc_log.txt"
    # Удаляем файл, если он уже существует (на случай повторного использования)
    if os.path.exists(calc.log_file):
        os.remove(calc.log_file)
    yield calc
    # Финализатор: удаляем файл и проверяем
    if os.path.exists(calc.log_file):
        os.remove(calc.log_file)
    assert not os.path.exists(calc.log_file), f"Файл {calc.log_file} не был удалён после теста"

@pytest.fixture(scope="function")
def calculator_with_memory(tmp_path):
    """Фикстура для создания экземпляра CalcWithMemory с предустановленным значением в памяти."""
    CalcWithMemory._instance = None
    calc = CalcWithMemory()
    calc.log_file = tmp_path / "calc_log.txt"
    # Удаляем файл, если он уже существует
    if os.path.exists(calc.log_file):
        os.remove(calc.log_file)
    calc.memo_plus(10)  # Предустановленное значение в памяти
    yield calc
    # Финализатор: удаляем файл и проверяем
    if os.path.exists(calc.log_file):
        os.remove(calc.log_file)
    assert not os.path.exists(calc.log_file), f"Файл {calc.log_file} не был удалён после теста"

@pytest.fixture(params=[
    (2, 2, 4.0),
    (3, 3, 9.0),
    (4, 5, 20.0),
    (1.5, 2, 3.0)
])
def multiplication_data(request):
    return request.param