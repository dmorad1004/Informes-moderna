import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

distances = np.arange(1, 11, 1.0)
powers = np.array([58.6, 33.7, 22.0, 15.0,
                  11.3, 8.6, 6.9, 5.5, 4.6, 3.8])/22

# Regresión lineal
slope, intercept = np.polyfit(np.log(distances), np.log(powers), 1)

slope, intercept, r_value, p_value, std_err = linregress(
    np.log(distances), np.log(powers))

print("Pendiente:", f"{slope} +- {std_err}")
print("Intercepto (log(C)):", intercept)
print("R^2 :", r_value*r_value)

# Graficar
fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.loglog(distances, powers, 'o', label='Datos')
ax.loglog(distances, np.exp(intercept) * distances ** slope,
          'r-', label=f'Ajuste: Pendiente {slope:.2f}')

# Aumentar la densidad de ticks en los ejes log-log

ax.set_xlabel("Log Distancia (cm)")
ax.set_ylabel("Log Potencia (mW)")

# ax.set_title(
# "Potencia en función de la distancia, a una temperatura constante", fontsize=16)
ax.legend(fontsize="small")


plt.tight_layout()
plt.savefig("../Plantilla/resultados/imagenes/distancia.png", dpi=300)
plt.show()


# tablas

data = {
    "Distancias(cm)": distances,
    "Potencias(mW)": powers
}


df = pd.DataFrame({
    'Distancias(cm)': distances,
    'Potencias(mW)': powers
})

latex_code = df.to_latex(index=False, column_format="|c|c|", escape=False)

latex_code = latex_code.replace("\\toprule", "\\hline")
latex_code = latex_code.replace("\\midrule", "\\hline")
latex_code = latex_code.replace("\\bottomrule", "\\hline")

# Mostrar el código LaTeX
print(latex_code)
