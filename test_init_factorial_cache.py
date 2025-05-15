import pytest
from calculator.calculator.factorial_timer import init_factorial_cache, cached_factorial

def test_init_factorial_cache():
    init_factorial_cache(5)
    assert len(cached_factorial.cache_dict) == 6, "Кэш должен содержать 6 значений (0 до 5)"
    assert cached_factorial(3) == 6, "3! должно быть 6"


def test_negative_init_factorial_cache():
    with pytest.raises(ValueError):
        init_factorial_cache(-1)
    with pytest.raises(TypeError):
        init_factorial_cache("string")