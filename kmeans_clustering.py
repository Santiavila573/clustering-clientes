import numpy as np  # Importar la biblioteca NumPy para operaciones numéricas
import pandas as pd  # Importar la biblioteca pandas para manipulación de datos
import matplotlib.pyplot as plt  # Importar matplotlib para crear visualizaciones
from sklearn.cluster import KMeans  # Importar el modelo KMeans de scikit-learn para clustering

# Crear un DataFrame simulado de clientes
data = {
    'Frecuencia de Compras': [1, 2, 3, 4, 5, 1, 6, 2, 3, 5, 4, 7, 1, 3, 2],
    'Monto Gastado': [10, 5, 30, 40, 50, 15, 60, 25, 35, 55, 45, 70, 5, 30, 25]
}

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data)

# Definir el número de clusters (grupos) que queremos identificar
k = 3
# Inicializar el modelo KMeans con el número de clusters y una semilla aleatoria
kmeans = KMeans(n_clusters=k, random_state=42)
# Ajustar el modelo a los datos
kmeans.fit(df)

# Obtener las etiquetas (a qué cluster pertenece cada punto) y los centros de los clusters
labels = kmeans.labels_  # Etiquetas asignadas a cada punto
centers = kmeans.cluster_centers_  # Coordenadas de los centros de los clusters

# Configurar la visualización de los clusters
plt.figure(figsize=(8, 6))  # Definir el tamaño de la figura
# Graficar los puntos, coloreándolos según su cluster
plt.scatter(df['Frecuencia de Compras'], df['Monto Gastado'], 
            c=labels, cmap='viridis', marker='o', edgecolor='k', s=100)
# Graficar los centros de los clusters
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centros')
# Títulos y etiquetas de los ejes
plt.title('K-Means Clustering de Clientes')
plt.xlabel('Frecuencia de Compras')
plt.ylabel('Monto Gastado')
# Mostrar la leyenda
plt.legend()
# Mostrar la cuadrícula en la gráfica
plt.grid()
# Mostrar la gráfica
plt.show()