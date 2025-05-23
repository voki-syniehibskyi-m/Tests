import pytest

@pytest.mark.critical
def test_add_numbers(calculator):
    result = calculator.add(5, 5)
    assert result == 10

def test_argument_is_iter(calculator):
    result = calculator.add([1,2,3])
    assert result == 6

def test_one_argument_is_nan(calculator):
    result = calculator.add([], 2)
    assert result == 2

def test_invalid_iterable_input(calculator):
    with pytest.raises(TypeError):
        calculator.add(5)


