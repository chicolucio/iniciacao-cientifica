"""Testes feitos com valores do exemplo 16.2 do livro do McQuarrie"""

from van_der_waals import van_der_waals, Q_
import numpy as np


def test_valores_exemplo():
    a = Q_(5.5088, 'atm * dm**6 / mol**2')
    b = Q_(0.065144, 'dm**3 / mol')
    temperatura = Q_(300, 'K')
    pressao = Q_(200, 'atm')
    resposta_esperada = Q_(0.096, 'l / mol')
    assert np.isclose(van_der_waals(a, b, temperatura, pressao), resposta_esperada, atol=0.001)


def test_valores_exemplo_a_unidade_pressao_bar():
    a = Q_(5.5818, 'bar * dm**6 / mol**2')
    b = Q_(0.065144, 'dm**3 / mol')
    temperatura = Q_(300, 'K')
    pressao = Q_(200, 'atm')
    resposta_esperada = Q_(0.096, 'l / mol')
    assert np.isclose(van_der_waals(a, b, temperatura, pressao), resposta_esperada, atol=0.001)


def test_valores_exemplo_a_unidade_pressao_pascal():
    a = Q_(5.5818, 'bar * dm**6 / mol**2')
    b = Q_(0.065144, 'dm**3 / mol')
    temperatura = Q_(300, 'K')
    pressao = Q_(2.0265E7, 'Pa')
    resposta_esperada = Q_(0.096, 'l / mol')
    assert np.isclose(van_der_waals(a, b, temperatura, pressao), resposta_esperada, atol=0.001)
