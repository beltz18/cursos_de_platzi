# Assert Statements

Son expresiones, que combinan variables con operadores. El flujo sera aproximadamente como el siguiente:

* Código
  + Assert Statement
    - Error
    - Código

La forma de usarla en código es aún más sencilla:

```python
assert condition, error message
```

Sería algo como:

> Afirmo que esta condición es verdadera, sino, imprimo un mensaje de error

Ejemplo practico:

```python
def palindromo(string):
  assert len(string) > 0, "No se puede ingresar una cadena vacía"
  return string == string[::-1]

print(palindromo(""))
```

Salida:

>AssertionError: No se puede ingresar una cadena vacía

Funcionan igual que las excepciones: si la condición es verdadera se ejecuta el bloque de código, sino, eleva un error