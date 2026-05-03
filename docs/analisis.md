# Análisis del taller

## a. ¿Qué accuracy obtuvo el modelo?
El modelo obtuvo un accuracy de 0.9444 .

## b. ¿Qué variable aparece en la raíz del árbol?
La variable raíz del árbol es color_intensity (Intensidad de color)

## c. El modelo, ¿parece confiable?, justifique
el modelo tiene un accuracy de 0.9444 osea un 94.44% lo que me basta para decir que este modelo es confiables 


## d. ¿Se observa overfitting o underfitting?
No observo un overfitting o underfitting claro/fuerte principalmente por que el acurrey es del 94.44% por lo que descarto el underfitting , tampoco observo un overfitting por que estoy limitando el modelo a max_depth=3

## e. ¿Qué otras variables parecen más relevantes?
Las variables con mayor importancia en este árbol fueron:
- flavanoids
- color_intensity
- proline
- ash

## Nota
Las clases del dataset se representan como: class_0, class_1 y class_2 pero en el grafico la cambie por :Vino 1,Vino 2 ,Vino 3 este cambio lo hice por que facilita la interpretacion/leectura (solo por estetica)
