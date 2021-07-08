import numpy as np
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

GAS_CONSTANT = Q_(0.082057366080960, 'atm * l / (mol * K)')


@ureg.wraps('liter/mol', ('atm * dm**6 / mol**2', 'dm**3 / mol', 'K', 'atm'))
def van_der_waals(a, b, temperature, pressure):
    coef_V3 = 1
    coef_V2 = -(b + GAS_CONSTANT.magnitude * temperature / pressure)
    coef_V1 = a / pressure
    coef_V0 = - a * b / pressure
    poly = np.polynomial.Polynomial((coef_V0, coef_V1, coef_V2, coef_V3))
    raiz = poly.roots()

    return raiz[np.isreal(raiz)]
