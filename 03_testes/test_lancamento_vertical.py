from lancamento_vertical import altura
from pytest import approx


def test_tempo_0_velocidade_inicial_0():
    assert altura(5, 0, 0) == 5


def test_tempo_0_velocidade_inicial_1():
    assert altura(5, 1, 0) == 5


def test_velocidade_inicial_0_altura_inicial_0_tempo_1():
    assert altura(0, 0, 1) == -4.9


def test_velocidade_inicial_0_altura_inicial_0_tempo_2():
    assert altura(0, 0, 2) == -19.6


def test_velocidade_inicial_0_altura_inicial_1_tempo_2():
    assert altura(1, 0, 2) == -18.6


def test_velocidade_inicial_1_altura_inicial_0_tempo_1():
    assert altura(0, 1, 1) == approx(-3.9, rel=0, abs=0.001)
