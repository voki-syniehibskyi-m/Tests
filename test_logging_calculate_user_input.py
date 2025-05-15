import pytest
from calculator.calculator.basic_calc import BasicCalc
from unittest.mock import patch, mock_open


def test_logging_calculate_user_input_success(tmp_path):
    calc = BasicCalc()
    log_file = tmp_path / "calc_log.txt"

    # Мокаем open, чтобы писать в tmp_path/calc_log.txt
    mock_file = mock_open()
    with patch('builtins.open', mock_file):
        with patch('builtins.input', return_value="5+3"):
            result = calc.calculate_user_input()
            assert result == 8.0

    # Проверяем, что open вызывался с правильным файлом
    mock_file.assert_called_with('calc_log.txt', 'a', encoding='utf-8')

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


def test_logging_calculate_user_input_invalid(tmp_path):
    calc = BasicCalc()
    log_file = tmp_path / "calc_log.txt"

    # Мокаем open
    mock_file = mock_open()
    with patch('builtins.open', mock_file):
        with patch('builtins.input', side_effect=["abc+3", "5+3"]):
            result = calc.calculate_user_input()
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