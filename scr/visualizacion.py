from sklearn import tree
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

plt.style.use('seaborn-v0_8')


mpl.rcParams.update({'font.size': 10, 'figure.titlesize': 16})

# Mapeo de nombres de variables a español (editar según columnas reales)
feature_name_map = {
	'alcohol': 'Nivel de alcohol',
	'malic_acid': 'Ácido málico',
	'ash': 'Ceniza',
	'alcalinity_of_ash': 'Alcalinidad de la ceniza',
	'magnesium': 'Magnesio',
	'total_phenols': 'Fenoles totales',
	'flavanoids': 'Flavonoides',
	'nonflavanoid_phenols': 'Fenoles no flavonoides',
	'proanthocyanins': 'Proantocianidinas',
	'color_intensity': 'Intensidad de color',
	'hue': 'Matiz',
	'od280/od315_of_diluted_wines': 'OD280/OD315 (vinos diluidos)',
	'proline': 'Prolina',
}


def plot_decision_tree():
	"""Dibuja el árbol de decisión entrenado en `modelo.py`.

	Importa los objetos desde `modelo` en tiempo de ejecución para evitar
	ejecutar código de trazado cuando este módulo sea importado.
	"""
	try:
		from modelo import model, x_test, y_test, x, y
	except Exception as e:
		raise RuntimeError('No se pudieron importar variables desde modelo.py: ' + str(e))

	feature_names_es = [feature_name_map.get(col, col) for col in x.columns]
	class_labels = ['Vino 0', 'Vino 1', 'Vino 2']

	fig, ax = plt.subplots(figsize=(14, 10))
	plt.set_cmap('Pastel1')
	tree.plot_tree(
		model,
		filled=True,
		feature_names=feature_names_es,
		class_names=class_labels,
		proportion=True,
		rounded=True,
		precision=2,
		fontsize=10,
		ax=ax,
	)
	ax.set_title('Árbol de decisión — Clasificación de vinos', pad=18)
	plt.tight_layout()
	plt.show()
