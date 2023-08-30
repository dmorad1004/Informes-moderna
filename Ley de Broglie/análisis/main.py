import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

L = 13.5  # cm
PLANK_CONSTANT = 6.63e-34  # J*s
ELECTRON_CHARGE = 1.60e-19  # C
ELECTRON_MASS = 9.11e-31

# Datos medidos
voltages = np.array([2.8, 3.0, 3.3, 3.5, 3.7, 4.0,
                    4.3, 4.5, 4.7, 5.0])*1000  # kV
inner_ring = {
    "inner_diameter":
    np.array([2.55, 2.30, 2.25, 2.10, 2.10, 2.05, 1.95, 2.00, 2.00, 1.95]),
    "outer_diameter":
    np.array([3.00, 2.85, 2.65, 2.50, 2.60, 2.50, 2.03, 2.25, 2.03, 2.20])
}
outer_ring = {
    "inner_diameter":
    np.array([4.80, 4.70, 4.20, 4.25, 4.05, 4.00, 3.90, 3.80, 3.65, 3.70]),
    "outer_diameter":
    np.array([5.0, 5.20, 4.80, 4.60, 4.45, 4.40, 4.25, 4.30, 4.10, 4.10])
}


# Cálculos
average_inner_ring = (
    inner_ring["inner_diameter"]+inner_ring["outer_diameter"])/2

average_outer_ring = (
    outer_ring["inner_diameter"]+outer_ring["outer_diameter"])/2

inner_ring_angles = np.arctan(average_inner_ring/(2*L))/2
outer_ring_angles = np.arctan(average_outer_ring/(2*L))/2

sin_inner_ring = np.sin(inner_ring_angles)
sin_outer_ring = np.sin(outer_ring_angles)


electron_volt_list = voltages*ELECTRON_CHARGE
root_electron_volt_list = np.sqrt(electron_volt_list)

# regresión lineal

slope_inner, intercept_inner, r_value_inner, p_value_inner, std_err_inner = linregress(
    1/root_electron_volt_list, sin_inner_ring)
slope_outer, intercept_outer, r_value_outer, p_value_outer, std_err_outer = linregress(
    1/root_electron_volt_list, sin_outer_ring)

# Graficar

fig, ax = plt.subplots(2, 1)

ax[0].scatter(1/root_electron_volt_list, sin_inner_ring)
ax[0].plot(1/root_electron_volt_list, slope_inner *
           (1/root_electron_volt_list) + intercept_inner)

ax[1].scatter(1/root_electron_volt_list, sin_outer_ring)
ax[1].plot(1/root_electron_volt_list, slope_outer *
           (1/root_electron_volt_list) + intercept_outer)

plt.show()


interplanar_distance1 = PLANK_CONSTANT/(2*slope_inner*np.sqrt(2*ELECTRON_MASS))
interplanar_distance2 = PLANK_CONSTANT/(2*slope_outer*np.sqrt(2*ELECTRON_MASS))

print(interplanar_distance1)
print(interplanar_distance2)


# df = pd.DataFrame({
#     'Temperatura(K)': 1,
#     'Potencias(mW)': 1,
# })
#
#
# latex_code = df.to_latex(index=False, column_format="|c|c|", escape=False)
#
# latex_code = latex_code.replace("\\toprule", "\\hline")
# latex_code = latex_code.replace("\\midrule", "\\hline")
# latex_code = latex_code.replace("\\bottomrule", "\\hline")

# Mostrar el código LaTeX
# print(latex_code)
