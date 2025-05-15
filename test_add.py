import pytest
from calculator.calculator.basic_calc import BasicCalc

@pytest.mark.critical
def test_add_numbers():
    calc = BasicCalc()
    result = calc.add(5, 5)
    assert result == 10

def test_argument_is_iter():
    calc = BasicCalc()
    result = calc.add([1,2,3])
    assert result == 6

def test_one_argument_is_nan():
    calc = BasicCalc()
    result = calc.add([], 2)
    assert result == 2

def test_invalid_iterable_input():
    calc = BasicCalc()
    with pytest.raises(TypeError):
        calc.add(5)


