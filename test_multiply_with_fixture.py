import pytest


def test_multiply_with_fixture_parametrized(multiplication_data):
    a, b, expected = multiplication_data
    assert a * b == expected