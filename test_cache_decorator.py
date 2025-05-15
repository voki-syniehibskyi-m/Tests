from calculator.calculator.factorial_timer import cache

def test_cache_decorator():
    @cache
    def test_func(x):
        return x + 1
    test_func(5)
    assert len(test_func.cache_dict) == 1
    assert test_func(5) == 6

def test_negative_cache_decorator_missing_key():
    @cache
    def test_func(x):
        return x + 1
    assert 10 not in test_func.cache_dict, "Кэш не должен содержать ключ 10 до вызова"
    result = test_func(10)
    assert result == 11, "Результат должен быть 10 + 1 = 11"
    assert 10 in test_func.cache_dict, "Кэш должен содержать ключ 10 после вызова"
    assert test_func.cache_dict[10] == 11, "Значение в кэше должно быть 11"