from modelo import model, x_test, y_test
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Hacer predicciones
y_pred= model.predict(x_test)


y_pred= model.predict(x_test)
accuracy= accuracy_score(y_test, y_pred)
print(f'Accuracy del modelo: {accuracy:.2f}')
#analisis del desempeño del modelo
print('Reporte de clasificación:')
print(classification_report(y_test, y_pred))
