GRAVIDADE = 9.8  # m/s^2


def altura(altura_inicial, velocidade_inicial, tempo):
    return (altura_inicial +
            velocidade_inicial * tempo -
            1/2 * GRAVIDADE * tempo**2)
