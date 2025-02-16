# Segmentación de Clientes con K-Means

## 🚀 Funcionamiento

El programa sigue estos pasos:

1. **Definir el Problema**  
   Se establece el objetivo de agrupar clientes según su comportamiento de compra.

2. **Simular Datos**  
   Se crean datos simulados que representan la frecuencia de compras y el monto gastado de diferentes clientes.

3. **Preprocesar los Datos**  
   Se pueden normalizar los datos si es necesario (aunque en este ejemplo se utilizan directamente).

4. **Aplicar K-Means**  
   Se utiliza el algoritmo K-Means para agrupar los datos en clústeres.

5. **Mostrar Resultados**  
   El programa imprime los clientes junto con el clúster al que pertenecen.

## 📦 Requisitos

Antes de ejecutar el programa, asegúrate de tener instaladas las siguientes librerías:

- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`

### Instalación de Librerías

Puedes instalar las librerías necesarias utilizando `pip`. Abre tu terminal y ejecuta:

```bash
pip install numpy pandas matplotlib scikit-learn.
## ⚠️ Consideraciones

- Asegúrate de tener Python instalado en tu sistema.
- Al trabajar con datos simulados, verifica que los datos generados sean representativos para obtener resultados significativos.
- Si decides normalizar los datos, considera el impacto que esto puede tener en el rendimiento del algoritmo K-Means.

## 📊 Resultados

Al ejecutar el programa, los clientes se agruparán en clústeres. Por ejemplo:

- **Clúster 0**: Clientes que compran frecuentemente pero gastan poco.
- **Clúster 1**: Clientes que compran ocasionalmente y gastan moderadamente.
- **Clúster 2**: Clientes que compran con frecuencia y gastan mucho.

Cada grupo representa un comportamiento de compra similar.

## 📝 Conclusión

Hemos utilizado K-Means y datos simulados para agrupar clientes según su frecuencia de compras y el monto gastado. Este enfoque es útil para segmentar clientes y desarrollar estrategias de marketing personalizadas.
