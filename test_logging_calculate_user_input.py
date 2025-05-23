import pytest
from calculator.calculator.basic_calc import BasicCalc
from unittest.mock import patch, mock_open


def test_logging_calculate_user_input_success(calculator, tmp_path):
    # Мокаем open для calc.log_file
    mock_file = mock_open()
    with patch('builtins.open', mock_file):
        with patch('builtins.input', return_value="5+3"):
            result = calculator.calculate_user_input()
            assert result == 8.0

    # Проверяем, что open вызывался с правильным файлом (calc.log_file)
    mock_file.assert_called_with(calculator.log_file, 'a', encoding='utf-8')

    # Проверяем, что данные записаны
    written_data = "".join(call.args[0] for call in mock_file().write.call_args_list)
    assert "Operation: UserInput" in written_data
    assert "Arguments: ('5+3',)" in written_data
    assert "Result: Parsed" in written_data
    assert "Operation: Add" in written_data
    assert "Arguments: (5.0, 3.0)" in written_data
    assert "Result: 8.0" in written_data
    assert "Operation: CalculateUserInput" in written_data
    assert "Arguments: ()" in written_data
    assert "Result: 8.0" in written_data
    assert written_data.count("Log Entry:") == 3


def test_logging_calculate_user_input_invalid(calculator, tmp_path):

    # Мокаем open
    mock_file = mock_open()
    with patch('builtins.open', mock_file):
        with patch('builtins.input', side_effect=["abc+3", "5+3"]):
            result = calculator.calculate_user_input()
            assert result == 8.0

    # Проверяем, что данные записаны
    written_data = "".join(call.args[0] for call in mock_file().write.call_args_list)
    assert "Operation: UserInput" in written_data
    assert "Arguments: ('abc+3',)" in written_data
    assert "Error: Invalid expression" in written_data
    assert "Arguments: ('5+3',)" in written_data
    assert "Result: Parsed" in written_data
    assert "Operation: Add" in written_data
    assert "Operation: CalculateUserInput" in written_data
    assert written_data.count("Log Entry:") == 4