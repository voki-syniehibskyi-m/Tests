import pytest


@pytest.mark.critical
def test_multiply_nums(calculator):
    result = calculator.multiply(5, 5)
    assert result == 25

def test_negative_multiply_nums(calculator):
    result = calculator.multiply(5, 'string')
    assert result == 0



