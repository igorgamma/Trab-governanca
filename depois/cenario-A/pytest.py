import pytest

from sensor_query import calcular_emissao_co2


def test_calculo_normal():

    resultado = calcular_emissao_co2(100)

    assert resultado == 8.17


def test_calculo_zero():

    resultado = calcular_emissao_co2(0)

    assert resultado == 0


def test_calculo_negativo():

    with pytest.raises(ValueError):
        calcular_emissao_co2(-10)
