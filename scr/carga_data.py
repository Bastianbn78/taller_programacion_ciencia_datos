from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine()
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)

# print(f'i. primeros registros \n {df_wine.head()}')
# print(f'ii. Nombres de variables \n {df_wine.columns}')
# print(f'iii. clases de vino \n {wine.target_names}')
# print(f'iv. cantidad de datos \n {df_wine.shape[0]}')
# print(f'v. Estadisticas \n {df_wine.describe()}')
# print(wine.target_names)#tipos de vinos
df_wine['target'] = wine.target