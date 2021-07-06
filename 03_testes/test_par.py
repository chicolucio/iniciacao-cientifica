from par import eh_par


def test_4_verdadeiro():
    assert eh_par(4)


def test_5_falso():
    assert not eh_par(5)
