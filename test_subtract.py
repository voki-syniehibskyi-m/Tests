import pytest

@pytest.mark.xfail
@pytest.mark.critical
def test_subtract_numbers(calculator):
    result = calculator.subtract(5,3)
    assert result == 2

@pytest.mark.xfail
def test_negative_subtract_numbers(calculator):
    result = calculator.subtract(5, 'str')
    assert result == 5

