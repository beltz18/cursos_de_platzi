# High Order Functions

###### filter, map y reduce

Son funciones que reciben como parametro, otra función. Un ejemplo claro de esto es:

```python
def saludo(func):
  func()

def hola():
  print('Hola!')

def adios():
  print('Adios!')

saludo(hola)
saludo(adios)
```

La función saludo recibe como parametro otra función, de esta forma, cuando se ejecuta dentro de saludo llama a esa función y la ejecuta.

## filter

Para problemas como el siguiente:

> ```[1,4,5,6,9,13,19,21]```

Donde se quiere extraer, por ejemplo, en una nueva lista todos los números excepto los que sean pares, se puede emplear las List Comprehensions. Quedaría algo así:

```python
myList = [1,4,5,6,9,13,19,21]
odd    = [i for i in myList if i % 2 != 0]

print(odd)
```

Esto puede ser resuelto con la función filter:

```python
myList = [1,4,5,6,9,13,19,21]
odd    = list(filter(lambda x: x%2 != 0, myList))

print(odd)
```

El resultado mostrado por pantalla en ambos casos sería:

> ```[1,5,9,13,19,21]```

Al final, la función filter recibe dos parametros: una función anónima y un iterable. Filter por defecto retorna un iterador.

## map

Si tenemos la siguiente lista:

> ```[1,2,3,4,5]```

y deseamos crear una nueva a partir de esta donde los valores estén aumentados al cuadrado. Podríamos resolverlo con List Comprehensions de la siguiente manera:

```python
myList = [1,2,3,4,5]
square = [i**2 for i in myList]

print(squares)
```

Esto puede ser resuelto de una manera más sencilla con **map**:

```python
myList = [1,2,3,4,5]
square = list(map(lambda x: x**2, myList))

print(squares)
```

El resultado mostrado por pantalla en ambos casos sería:

> ```[1,4,9,16,25]```

Map, al igual que filter, recibe dos parametros, pero, recibe una lista y retorna otra.

## reduce

Imaginemos que tenemos la siguiente lista:

> ```[2,2,2,2,2]```

y queremos multiplicar todos los valores para obtener el resultado. Podemos reducir el valor de la lista a uno solo mediante el siguiente código:

```python
myList = [2,2,2,2,2]
all_m  = 1

for i in myList:
  all_m *= i

print(all_m)
```

con la función reduce, el código quedaría de la siguiente manera:

```python
from functools import reduce

myList = [2,2,2,2,2]
all_m  = reduce(lambda a, b: a * b, myList)

print(all_m)
```

El resultado mostrado por pantalla en ambos casos sería:

> ```32```