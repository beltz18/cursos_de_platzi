# Errores en Python

Se pueden clasificar de forma general los errores en dos tipos:

- Cuando Python avisa que hay un error
- Y cuando no

* Errores:
  - SyntaxError
  - Exception
    + ImportError
    + ZeroDivisionError
    + FileNotFoundError
    + IndexError
    + KeyError
    + KeyboardInterrupt
    + ...

Cuando Python no avisa un error suele tener que ver con un error de código por parte nuestra, suelen ser de lógica y para resolverlos se debe revisar exhaustivamente el programa de principio a fín para resolverlo de forma más eficiente. También se pueden usar tecnicas de debugging o softwares especializados para vigilar el comportamiento del código.

Cuando Python nos avisa, devuelve un Traceback, que es algo como lo siguiente:

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>**ZeroDivisionError**: division by zero

Que es el error que obtenemos cuando tratamos de hacer una división entre cero.

La mejor forma de leer este tipo de errores es de abajo hacia arriba. De la siguiente forma:

- El error es causado por intentar dividir entre cero.
- El archivo donde ocurrió el error, la linea y el modulo.
- La traza donde ocurrió el error.

## SyntaxError

Normalmente, cuando nos encontramos con errores de Sintaxis, Python no ejecuta el programa y espera a que sea resuelto para ejecutarlo. Ejemplo de Error de sintaxis: en vez de **for** escribir **far**.

## Exception

Las Excepciones o typos son errores que permiten la ejecución del código pero, al llegar a una línea afectada, este se rompe y eleva un error hasta un punto superior para detener el programa. Un ejemplo de esto es, cuando se pulsa **Ctrl + C** en medio de la ejecución de un archivo de Python en la terminal.