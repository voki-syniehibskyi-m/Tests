from calculator.calculator.collections_random import random_numbers, amount_of_nums, min_value, max_value
import pytest
def test_random_number_length():
    assert len(random_numbers) == amount_of_nums

def test_random_numbers_range():
    assert all(min_value <= x <= max_value for x in random_numbers)

def test_random_numbers_range_invalid():
    invalid_values = [0, 11]  # Значения вне [1, 10]
    assert not any(x in invalid_values for x in random_numbers)

