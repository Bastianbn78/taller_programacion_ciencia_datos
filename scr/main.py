import os
os.system('cls')  # Limpiar la consola al iniciar
# ============================================================================
# ANÁLISIS EXPLORATORIO DE DATOS
# ============================================================================
from sklearn.datasets import load_wine
import pandas as pd

print("=" * 70)
print("ANÁLISIS EXPLORATORIO DE DATOS - DATASET WINE")
print("=" * 70)

wine = load_wine()
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)

print(f'\n i. Primeros registros:\n {df_wine.head()}')
print(f'\n ii. Nombres de variables:\n {df_wine.columns.tolist()}')
print(f'\n iii. Clases de vino:\n {wine.target_names}')
print(f'\n iv. Cantidad de datos:\n {df_wine.shape[0]} registros, {df_wine.shape[1]} características')
print(f'\n v. Estadísticas descriptivas:\n {df_wine.describe()}')

df_wine['target'] = wine.target

# ============================================================================
# ENTRENAMIENTO DEL MODELO
# ============================================================================
print("\n" + "=" * 70)
print("ENTRENAMIENTO DEL MODELO - ÁRBOL DE DECISIÓN")
print("=" * 70)

from modelo import model, x_test, y_test, x, y
print("\n✓ Modelo entrenado exitosamente.")
print(f"  - Características utilizadas: {x.shape[1]}")
print(f"  - Datos de prueba: {x_test.shape[0]} registros")

# ============================================================================
# VISUALIZACIÓN DEL MODELO
# ============================================================================
print("\n" + "=" * 70)
print("VISUALIZACIÓN - ÁRBOL DE DECISIÓN")
print("=" * 70)


# ============================================================================
# EVALUACIÓN DEL MODELO
# ============================================================================
print("\n" + "=" * 70)
print("EVALUACIÓN DEL DESEMPEÑO DEL MODELO")
print("=" * 70)

from sklearn.metrics import accuracy_score, classification_report

# Hacer predicciones
y_pred = model.predict(x_test)

# Calcular accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'\n✓ Accuracy del modelo: {accuracy:.4f} ({accuracy*100:.2f}%)')

# Reporte detallado de clasificación
print('\n✓ Reporte de clasificación:')
print(classification_report(y_test, y_pred, target_names=wine.target_names))

# ============================================================================
# RESUMEN FINAL
# ============================================================================
print("\n" + "=" * 70)
print("RESUMEN FINAL")
print("=" * 70)
n_train = int(df_wine.shape[0] * 0.8)
print(f"✓ Dataset cargado: {df_wine.shape[0]} muestras")
print(f"✓ Modelo entrenado con {n_train} muestras (80%)")
print(f"✓ Evaluado en {x_test.shape[0]} muestras de prueba (20%)")
print(f"✓ Desempeño final: {accuracy*100:.2f}% de precisión")
print("=" * 70)

# =====================
# VISUALIZACIÓN FINAL
# =====================
print('\nMostrando visualización del árbol de decisión (final)...')
from visualizacion import plot_decision_tree
plot_decision_tree()


