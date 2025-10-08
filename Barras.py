import matplotlib.pyplot as plt
import numpy as np

# Datos
tazas = ["0", "1", "3", "4"]
respuestas = [2, 4, 3, 2]

# Crear posición de las barras
x = np.arange(len(tazas))

# Crear la gráfica de barras con colores diferentes
colores = ['#8B4513', '#D2691E', '#CD853F', '#F4A460']  # tonos tipo café

plt.bar(x, respuestas, color=colores, width=0.6, edgecolor="black")

# Etiquetas
plt.xticks(x, tazas)
plt.xlabel("Tazas de café al día", fontsize=12)
plt.ylabel("Número de personas", fontsize=12)
plt.title("¿Cuántas tazas de café tomas al día?", fontsize=14, fontweight='bold', color='blue')

# Mostrar los valores arriba de cada barra
for i, v in enumerate(respuestas):
    plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

# Estilo de cuadrícula
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
