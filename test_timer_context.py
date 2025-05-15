import pytest
from calculator.calculator.factorial_timer import Timer
import time

def test_timer_context():
    with Timer() as t:
        time.sleep(0.1)
    assert t.elapsed_time >= 0.1



def test_timer_context_invalid():
    with pytest.raises(ValueError):
        with Timer() as t:
            raise ValueError("Симуляция ошибки внутри контекста")

