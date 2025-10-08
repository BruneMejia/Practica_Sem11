import matplotlib.pyplot as plt

# Datos reales de la encuesta
# 4 personas dijeron 60 min, 2 dijeron 15 min, 1 dijo que 30min, 1 dijo que 2h con 30 min, 1 dijo 120 min
tiempos = [60, 60, 60, 60, 15, 15, 45, 45, 30, 150, 120]

# Crear el histograma
plt.hist(tiempos, bins=6, color='skyblue', edgecolor='black')

# Personalizar el gráfico
plt.title("Tiempo que tardan los estudiantes en llegar a la Universidad")
plt.xlabel("Minutos")
plt.ylabel("Número de estudiantes")

# Mostrar el histograma
plt.show()

