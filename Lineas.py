import matplotlib.pyplot as plt

# Datos
tazas = [0, 1, 3, 4]
respuestas = [2, 4, 3, 2]

# Crear la gráfica
plt.plot(tazas, respuestas, label="Cantidad de respuestas", color="brown", marker="o", linewidth=2)

# Título y etiquetas
plt.title("¿Cuántas tazas de café tomas al día?", fontsize=14, fontweight='bold')
plt.xlabel("Tazas de café al día", fontsize=12)
plt.ylabel("Número de personas", fontsize=12)

# Personalización del fondo y estilo
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar la gráfica
plt.show()
