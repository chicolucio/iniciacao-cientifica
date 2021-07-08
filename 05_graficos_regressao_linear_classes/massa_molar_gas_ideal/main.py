import numpy as np
import matplotlib.pyplot as plt
import pint
from scipy.constants import gas_constant
from scipy.stats import linregress
from helpers import replace_comma_to_dot, plot_params


ureg = pint.UnitRegistry()
ureg.setup_matplotlib()
gas_constant = gas_constant * ureg('J/(mol*K)')
temperature = 300 * ureg.kelvin


dados = np.genfromtxt((replace_comma_to_dot(text) for text in open('dados.csv')),
                      delimiter=';', dtype=(float, float), names=['P_bar', 'd_gL'], skip_header=1)

valores_pressao = dados['P_bar'] * ureg.bar
valores_densidade = dados['d_gL'] * ureg('g/l')
pressao_sobre_densidade = valores_pressao / valores_densidade
regressao = linregress(valores_densidade.magnitude, pressao_sobre_densidade.magnitude)
massa_molar = gas_constant * temperature / (regressao.intercept * ureg('bar / (g/l)'))

fig, ax = plt.subplots(figsize=(8, 6), nrows=1, ncols=1, tight_layout=True)
plot_params(ax)
x = np.linspace(valores_densidade[0].magnitude, valores_densidade[-1].magnitude, 50)
y = regressao.slope * x + regressao.intercept
ax.plot(x, y, color='red', zorder=-1)
ax.scatter(valores_densidade, pressao_sobre_densidade, s=60)
ax.set_xlabel(r'$\rho$ / $g \cdot \ell^{-1}$', fontsize=18)
ax.set_ylabel(r'$\frac{P}{\rho}$ / $bar \cdot \ell \cdot g^{-1}$', fontsize=18)
ax.text(2, 0.56, f'y = {regressao.slope:.3e}x + {regressao.intercept:.3e}', fontsize=14, bbox=dict(facecolor='red', alpha=0.9))

print(massa_molar.to('g/mol'))
plt.show()
