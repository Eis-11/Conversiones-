import pytest
from Conversion import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    km_a_millas,
    millas_a_km,
    kg_a_libras,
)


def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32
    assert celsius_a_fahrenheit(100) == 212


def test_fahrenheit_a_celsius():
    assert fahrenheit_a_celsius(32) == 0
    assert fahrenheit_a_celsius(212) == 100


def test_km_a_millas():
    assert km_a_millas(10) == pytest.approx(6.21371)


def test_millas_a_km():
    assert millas_a_km(6.21371) == pytest.approx(10)


def test_kg_a_libras():
    assert kg_a_libras(1) == pytest.approx(2.20462)