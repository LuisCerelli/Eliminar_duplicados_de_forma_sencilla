## Eliminación de Elementos Duplicados en una Lista
### Descripción
Este script en Python tiene como objetivo eliminar los elementos duplicados de una lista, manteniendo el orden de aparición de los elementos. Se toma una lista original y se crea una lista auxiliar donde solo se agregan los elementos que no se han añadido previamente. De esta manera, se obtiene una nueva lista que contiene los mismos elementos que la original, pero sin duplicados.

### Funcionamiento
1. Entrada: Se parte de una lista predefinida con valores que pueden estar duplicados.
2. Proceso: Se itera sobre cada elemento de la lista original y, mediante un condicional (if), se verifica si dicho elemento ya ha sido agregado a una lista auxiliar. Si no está en la lista auxiliar, se añade.
3. Salida: El script muestra por pantalla la lista original y la nueva lista sin elementos duplicados.
### Ejemplo de uso:
Supongamos que tenemos la lista:

```
[3, 3, 5, 1, 4, 5, 1, 1, 4, 5, 7, 8, 3]
```

Tras ejecutar el código, el resultado será:

```
La lista inicial es:  [3, 3, 5, 1, 4, 5, 1, 1, 4, 5, 7, 8, 3]
La lista sin duplicados es:  [3, 5, 1, 4, 7, 8]
```
### Aplicaciones en Ingeniería de Datos
***En el ámbito de la ingeniería de datos, este código puede ser particularmente útil en procesos de limpieza y preprocesamiento de datos. Al eliminar duplicados de una lista o conjunto de datos, es posible optimizar la cantidad de información que se procesa, reduciendo redundancias y mejorando la calidad de los datos. Este tipo de operaciones es esencial en tareas como la deduplicación de registros o la normalización de datos, permitiendo un análisis más preciso y eficiente.***
### Consideraciones:
Este enfoque garantiza que los elementos únicos de la lista se mantengan en el mismo orden en el que aparecen por primera vez en la lista original.
El código es adecuado para listas pequeñas o medianas, pero en casos de grandes volúmenes de datos, se recomienda considerar soluciones más eficientes, como el uso de estructuras de datos especializadas (por ejemplo, conjuntos en Python).
