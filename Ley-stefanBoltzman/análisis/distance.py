import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

distances = np.arange(1, 11, 1.0)
powers = np.array([58.6, 33.7, 22.0, 15.0,
                  11.3, 8.6, 6.9, 5.5, 4.6, 3.8])/22

# Regresión lineal
slope, intercept = np.polyfit(np.log(distances), np.log(powers), 1)

print("Pendiente:", slope)
print("Intercepto (log(C)):", intercept)

# Graficar
fig, ax = plt.subplots()

ax.loglog(distances, powers, 'o', label='Datos')
ax.loglog(distances, np.exp(intercept) * distances ** slope,
          'r-', label=f'Ajuste: Pendiente {slope:.2f}')

ax.set_xlabel("Distancia (cm)", fontsize=14)
ax.set_ylabel("Potencia (mW)", fontsize=14)

ax.set_title(
    "Potencia en función de la distancia, a una temperatura constante", fontsize=16)
ax.legend()

plt.savefig("../Plantilla/resultados/imagenes/distancia.png")
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
