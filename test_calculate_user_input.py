from unittest.mock import patch
import pytest


@pytest.mark.xfail
@pytest.mark.parametrize("user_input, expected_result", [
    ("5+3", 8.0),          # Позитивный случай: сложение
    ("10-4", 6.0),         # Позитивный случай: вычитание
    ("4*2", 8.0),          # Позитивный случай: умножение
    ("6/2", 3.0),          # Позитивный случай: деление
    ("5.5+2.5", 8.0)      # Позитивный случай: числа с плавающей точкой
])
@pytest.mark.critical
def test_positive_calculate_user_input(calculator, user_input, expected_result):
    with patch('builtins.input', return_value=user_input):
        result = calculator.calculate_user_input()
    assert result == expected_result


def test_negative_calculate_user_input(calculator):
    with patch('builtins.input', side_effect=['asd + 2', '2+2']):
        result = calculator.calculate_user_input()
    assert result == 4, 'После первого неудачного инпута, будет правильный 2+2'