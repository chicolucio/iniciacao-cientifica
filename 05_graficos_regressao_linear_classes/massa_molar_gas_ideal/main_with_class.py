import numpy as np
import matplotlib.pyplot as plt
import pint
from scipy.constants import gas_constant
from scipy.stats import linregress
from helpers import replace_comma_to_dot, plot_params


ureg = pint.UnitRegistry()
ureg.setup_matplotlib()
gas_constant = gas_constant * ureg('J/(mol*K)')


class IdealGas:

    def __init__(self, temperature, data_file):
        self.temperature = temperature
        self.data = self._data_from_file(data_file)

    @staticmethod
    def _data_from_file(data_file):
        return np.genfromtxt((replace_comma_to_dot(text) for text in
                              open(data_file)), delimiter=';',
                             dtype=(float, float),
                             names=['P_bar', 'd_gL'], skip_header=1)

    @property
    def pressure_data(self):
        return self.data['P_bar'] * ureg.bar

    @property
    def density_data(self):
        return self.data['d_gL'] * ureg('g/l')

    @property
    def regression(self):
        pressure_per_density = self.pressure_data / self.density_data
        return linregress(self.density_data.magnitude,
                          pressure_per_density.magnitude)

    @property
    def molar_mass(self):
        MM = gas_constant * self.temperature / \
            (self.regression.intercept * ureg('bar / (g/l)'))
        return MM.to('g/mol')

    def plot(self):
        fig, ax = plt.subplots(figsize=(8, 6), nrows=1,
                               ncols=1, tight_layout=True)
        plot_params(ax)

        x = np.linspace(
            self.density_data[0].magnitude,
            self.density_data[-1].magnitude, 50)
        y = self.regression.slope * x + self.regression.intercept
        pressure_per_density = self.pressure_data / self.density_data
        ax.plot(x, y, color='red', zorder=-1)

        ax.scatter(self.density_data, pressure_per_density, s=60)

        ax.set_xlabel(r'$\rho$ / $g \cdot \ell^{-1}$', fontsize=18)
        ax.set_ylabel(
            r'$\frac{P}{\rho}$ / $bar \cdot \ell \cdot g^{-1}$', fontsize=18)
        ax.text(2, 0.56,
                f'y = {self.regression.slope:.3e}x + {self.regression.intercept:.3e}',  # NOQA
                fontsize=14, bbox=dict(facecolor='red', alpha=0.9))
        plt.show()


if __name__ == '__main__':
    temperature = 300 * ureg.kelvin
    file = 'dados.csv'
    gas = IdealGas(temperature, file)
    print(gas.molar_mass)
    gas.plot()
