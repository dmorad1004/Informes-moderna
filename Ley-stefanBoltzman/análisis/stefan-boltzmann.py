import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

T_0 = 300  # K
R_O = 0.5  # ohms
STEFAN_BOLTZMANN_CONSTANT = 5.67e-8  # W/m^2K^4
TEMPERATURE_COEFFICIENT = 4.5e-3  # k^-1

currents = np.array([0.88, 1.06, 1.28, 1.51, 1.73])
voltages = np.array([3.0, 4.5, 6.5, 9.0, 11.8])

resistances = voltages/currents
filament_temperatures = T_0 + (resistances - R_O)/(TEMPERATURE_COEFFICIENT*R_O)

powers = np.array([12.3, 7.9, 7.2, 7.1, 7.1])/22

fig, ax = plt.subplots()

# Realizamos el ajuste lineal en el espacio log-log.

slope, intercept, r_value, p_value, std_err = linregress(
    np.log10(filament_temperatures), np.log10(powers))
# ax.plot(np.log10(filament_temperatures), slope*np.log10(filament_temperatures) +
# intercept, 'r', label=f'Pendiente = {slope:.2f}')

ax.scatter(filament_temperatures, powers, color="black")
ax.set_xlabel("Temperatura (K)", fontsize=14)
ax.set_ylabel("Potencia (mW)", fontsize=14)

ax.set_yscale("log")
ax.set_xscale("log")


ax.set_title("Potencia radiada en función de la temperatura", fontsize=18)

plt.savefig("../Plantilla/resultados/imagenes/stefan.png")

plt.show()

data = {
    "Temperatura(K)": filament_temperatures,
    "Potencias(mW)": powers
}


# Tablas

df = pd.DataFrame({
    'Temperatura(K)': filament_temperatures,
    'Potencias(mW)': powers
})

latex_code = df.to_latex(index=False, column_format="|c|c|", escape=False)

latex_code = latex_code.replace("\\toprule", "\\hline")
latex_code = latex_code.replace("\\midrule", "\\hline")
latex_code = latex_code.replace("\\bottomrule", "\\hline")

# Mostrar el código LaTeX
print(latex_code)

print(f"Pendiente: {slope:.4f}")
