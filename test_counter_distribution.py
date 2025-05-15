import pytest
from calculator.calculator.collections_random import counter, amount_of_nums

def test_counter_distribution():
    total_count = sum(counter.values())
    assert total_count == amount_of_nums

def test_negative_counter_distribution():
    counter.clear()
    with pytest.raises(TypeError):
        counter.update(5)

