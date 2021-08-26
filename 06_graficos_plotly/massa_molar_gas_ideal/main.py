import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
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

    @property
    def _experimental_data(self):
        pressure_per_density = self.pressure_data / self.density_data
        return self.density_data, pressure_per_density

    @property
    def _theoretical_data(self):
        x = np.linspace(self.density_data[0].magnitude,
                        self.density_data[-1].magnitude, 50)
        y = self.regression.slope * x + self.regression.intercept
        return x, y

    def _plot_matplotlib(self):
        fig, ax = plt.subplots(figsize=(8, 6), nrows=1,
                               ncols=1, tight_layout=True)
        plot_params(ax)

        ax.plot(*self._theoretical_data, color='red', zorder=-1)

        ax.scatter(*self._experimental_data, s=60)

        ax.set_xlabel(r'$\rho$ / $g \cdot \ell^{-1}$', fontsize=18)
        ax.set_ylabel(
            r'$\frac{P}{\rho}$ / $bar \cdot \ell \cdot g^{-1}$', fontsize=18)
        ax.text(2, 0.56,
                f'y = {self.regression.slope:.3e}x + {self.regression.intercept:.3e}',  # NOQA
                fontsize=14, bbox=dict(facecolor='red', alpha=0.9))
        plt.show()

    def _plot_plotly(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self._theoretical_data[0],
                                 y=self._theoretical_data[1],
                                 mode='lines',
                                 name='Linear fit',
                                 hovertemplate="%{x:.2f}, %{y:.4f}",
                                 ))
        fig.add_trace(go.Scatter(x=self._experimental_data[0],
                                 y=self._experimental_data[1],
                                 mode='markers',
                                 name='Experimental',
                                 marker=dict(size=10),
                                 hovertemplate="%{x:.2f}, %{y:.4f}",
                                 ))
        fig.update_layout(hovermode='closest')
        fig.update_xaxes(showspikes=True)
        fig.update_yaxes(showspikes=True)
        fig.update_layout(
            xaxis={'title': r'$\Large \rho / \text{g} \cdot \ell^{-1}$'},
            yaxis={'title': r'$\Large\frac{P}{\rho} / \text{bar} \cdot \ell \cdot \text{g}^{-1}$'},  # NOQA
            font={'size': 18},
            # template='plotly_dark',
            yaxis_tickformat='.4f',
            xaxis_tickformat='.2f',
        )
        fig.add_annotation(x=0.5, y=0.9,
                           text=f'y = {self.regression.slope:.3e}x + {self.regression.intercept:.3e}',  # NOQA
                           xref='paper', yref='paper', showarrow=False,
                           font=dict(color='white'), bgcolor='red',
                           opacity=0.8)
        fig.show()

    def plot(self, backend='matplotlib'):
        if backend == 'matplotlib':
            self._plot_matplotlib()
        elif backend == 'plotly':
            self._plot_plotly()
        else:
            raise ValueError('Invalid plot backend')


if __name__ == '__main__':
    temperature = 300 * ureg.kelvin
    file = 'dados.csv'
    gas = IdealGas(temperature, file)
    print(gas.molar_mass)
    # gas.plot()
    gas.plot('plotly')
