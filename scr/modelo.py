
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# Cargar los datos
from carga_data import df_wine
# Preparar los datos
x=df_wine[['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']]
y= df_wine['target']
# Dividir los datos en entrenamiento y prueba
x_train, x_test, y_train, y_test= train_test_split(x,y, test_size=0.2, random_state=42)
# Crear el modelo de árbol de decisión
model= DecisionTreeClassifier(max_depth=3, random_state=42)
# Entrenar el modelo
model.fit(x_train, y_train)
# Hacer predicciones
y_pred= model.predict(x_test)


