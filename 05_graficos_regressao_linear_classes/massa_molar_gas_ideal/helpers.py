def replace_comma_to_dot(string):
    return string.replace(',', '.').encode()


def plot_params(axis):
    ax = axis
    ax.grid(b=True, axis='both', which='major', linestyle='--', linewidth=1.5)
    ax.minorticks_on()
    ax.grid(b=True, which='minor', axis='both', linestyle=':', linewidth=1.0)
    ax.tick_params(axis='both', labelsize=16,
                   length=6, which='major', width=1.5)
    ax.tick_params(axis='both', length=3, which='minor', width=1.0)
    ax.set_axisbelow(True)
