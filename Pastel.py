import matplotlib.pyplot as plt

# Datos
redes = ["TikTok", "Instagram", "WhatsApp"]
respuestas = [6, 4, 1]

# Crear gráfica de pastel
plt.pie(
    respuestas, 
    labels=redes, 
    autopct="%1.1f%%",   # Mostrar porcentajes
    startangle=90,       # Comienza a dibujar desde arriba
    colors=["#66b3ff", "#ffcc99", "#c2c2f0"], 
    shadow=True
)

# Título
plt.title("¿Qué red social usas más?", fontsize=14, fontweight='bold')

# Mostrar gráfica
plt.show()
