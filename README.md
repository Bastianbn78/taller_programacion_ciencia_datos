# 🍷 Taller de Programación para Ciencia de Datos

**Entrega del primer taller de la materia Programación para Ciencia de Datos**

---

## 📋 Descripción del Proyecto

Este proyecto implementa un **análisis exploratorio de datos (EDA)** y un **modelo de Machine Learning** basado en clasificación de vinos. Utiliza el famoso dataset Wine de scikit-learn para entrenar un árbol de decisión que clasifica vinos en tres categorías diferentes con una precisión del 94.44%.

### 🎯 Objetivos
- Cargar y explorar un dataset de vinos
- Realizar análisis descriptivos de los datos
- Entrenar un modelo de árbol de decisión
- Evaluar el desempeño del modelo
- Visualizar los resultados

---

## 📁 Estructura del Proyecto

```
taller_programacion_ciencia_datos/
│
├── README.md                    # Este archivo
├── docs/
│   └── analisis.md             # Análisis detallado y conclusiones
│
└── scr/                         # Código fuente (scripts)
    ├── main.py                 # Script principal que orquesta todo
    ├── carga_data.py           # Carga y preparación de datos
    ├── modelo.py               # Entrenamiento del modelo
    ├── visualizacion.py        # Visualización del árbol de decisión
    └── Evaluacion.py           # Evaluación de métricas del modelo
```

---

## 🔧 Módulos del Proyecto

### `main.py` - Script Principal
- **Propósito**: Ejecutor central del proyecto
- Limpia la consola e importa todos los módulos
- Realiza análisis exploratorio de datos
- Visualiza y evalúa los resultados

### `carga_data.py` - Carga de Datos
- Importa el dataset Wine de scikit-learn
- Prepara los datos en DataFrames de pandas

### `modelo.py` - Entrenamiento
- Divide los datos en conjuntos de entrenamiento y prueba
- Entrena árbol de decisión (Decision Tree Classifier)
- Limita la profundidad del árbol a max_depth=3 para evitar overfitting
- Retorna el modelo entrenado y los datos separados

### `visualizacion.py` - Visualización
- Genera representaciones gráficas del árbol de decisión
- Renombra las clases (class_0, class_1, class_2) como Vino 1, Vino 2, Vino 3
- Facilita la interpretación visual del modelo

### `Evaluacion.py` - Métricas
- Calcula accuracy
- Evalúa la importancia de características

---

## 📊 Resultados Clave

| Métrica | Valor |
|---------|-------|
| **Accuracy** | 94.44% |
| **Variables más importantes** | flavanoids, color_intensity, proline, ash |
| **Variable raíz del árbol** | color_intensity (Intensidad de color) |
| **Profundidad máxima** | 3 niveles |

---

## 💡 Conclusiones

- El modelo demuestra ser **confiable** con un accuracy del 94.44%
- No se observa overfitting ni underfitting significativo
- La limitación de profundidad (max_depth=3) ayuda a mantener un modelo generalizado
- Las características de intensidad de color y flavanoides son las más discriminantes para clasificar vinos

Para más detalles, consulta [docs/analisis.md](docs/analisis.md)
