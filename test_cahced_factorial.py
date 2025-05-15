import pytest
from calculator.calculator.factorial_timer import cached_factorial, init_factorial_cache

def test_cached_factorial():
    init_factorial_cache(5)
    assert cached_factorial(5) == 120, "5! должно быть 120"
    assert cached_factorial(5) == cached_factorial.cache_dict[5], "Результат должен быть из кэша"

def test_negative_cached_factorial():
    with pytest.raises(ValueError, match="Факториал не определён для отрицательных чисел"):
        cached_factorial(-1)
    with pytest.raises(TypeError):
        cached_factorial("string")