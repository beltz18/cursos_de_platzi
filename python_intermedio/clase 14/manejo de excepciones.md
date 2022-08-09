# Manejo de Excepciones

## try except

El siguiente código:

```python
def palindromo(string):
  return string == string[::-1]

print(palindromo(1))
```

Arroja el siguiente error:

>>Traceback (most recent call last):
>>  File "main.py", line 4, in <module>
>>    print(palindromo(1))
>>  File "main.py", line 2, in palindromo 
>>    return string == string[::-1]
>>TypeError: 'int' object is not subscriptable

Y sucede porque la función no está protegida para cuando recibe un tipo de dato para el que no fue creada, o no espera el tipo de dato ingresado. Ya que, un número entero no se puede manejar como una cadena.

Para solucionar este problema se debe hacer lo siguiente:

```python
def palindromo(string):
  return string == string[::-1]

try
  print(palindromo(1))
except TypeError:
  print("Solo se pueden ingresar strings")
```

Aquí obtenemos la siguiente salida:

>> Solo se pueden ingresar strings

## raise

Qué pasa cuando, en el mismo ejemplo, el usuario no ingresa un tipo de dato equivocado sino, un espacio vacío:

```python
def palindromo(string):
  return string == string[::-1]

try
  print(palindromo(""))
except TypeError:
  print("Solo se pueden ingresar strings")
```

La salida de esta ejecución es la siguiente:

>>True

Y Python no se equivoca, la cadena vacía es igual a la cadena vacía inversa, pero, para fines practicos esto no puede ser calificado como un palíndromo. Entonces, la solución de este tipo de error es la siguiente:

```python
def palindromo(string):
  try:
    if len(string) == 0:
      raise ValueError("No se puede ingresar una cadena vacía")
    return string == string[::-1]
  except ValueError as ve:
    print(ve)
    return False

try
  print(palindromo(""))
except TypeError:
  print("Solo se pueden ingresar strings")
```

Aquí, acepta el valor de la cadena vacía pero eleva un error de valor con el mensaje:

>>No se puede ingresar una cadena vacía

Lo cual detiene la ejecución y finaliza el programa.

## finally

No se suele utilizar pero se utiliza al final de una estructura **try except**. Sus usos más comunes son: cerrar un archivo abierto por Python, cerrar una conexión a una base de datos o liberar recursos externos.

Un ejemplo claro es:

```python
try:
  f = open("archivo.txt")
finally:
  f.close()
```