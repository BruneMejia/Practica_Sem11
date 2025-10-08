import matplotlib.pyplot as plt

# Datos de la encuesta
horas_dormidas = [2, 5, 7, 8, 11]
respuestas = [2, 3, 4, 1, 1]

# Crear la gráfica lineal
plt.plot(horas_dormidas, respuestas, label="Cantidad de respuestas", color="navy", marker="o", linewidth=2)

# Título y etiquetas
plt.title("¿Cuántas horas dormiste anoche?", fontsize=14, fontweight='bold')
plt.xlabel("Horas de sueño", fontsize=12)
plt.ylabel("Número de personas", fontsize=12)

# Personalización
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar la gráfica
plt.show()
