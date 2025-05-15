from calculator.calculator.basic_calc import BasicCalc

def test_basic_calc_singleton():
    """Проверяет, что BasicCalc - это Singleton."""
    calc1 = BasicCalc()
    calc2 = BasicCalc()
    assert calc1 == calc2, "BasicCalc должен быть Singleton"

