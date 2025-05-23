import pytest


@pytest.mark.parametrize("user_input, expected_result", [
    ("5+3", 8.0),  # Сложение
    ("6*2", 12.0),  # Умножение
    ("15/3", 5.0),  # Деление
])
def test_positive_calculate_user_input(calculator, mocker, user_input, expected_result):
    # Мокаем input с помощью mocker
    mocker.patch('builtins.input', return_value=user_input)
    result = calculator.calculate_user_input()
    assert result == expected_result