# Debugging o Depuración

Existen diferentes herramientas o softwares de depuración que nos pueden ayudar para depurar nuestros programas en Python, VSC cuenta con uno integrado por defecto.

Un ejemplo de código malicioso donde podemos aplicar Debugging es el siguiente:

```python
def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 1]
  return divisors

def run():
  num = int(input("Ingresa un número: "))
  print(divisors(num))

if __name__ == '__main__':
  run()
```

El error de este programa se puede solucionar luego de usar el debugging y entrar dentro de la función divisors, ya que, para determinar que una división es exacta, esta debe dar como residuo 0, y nuestro residuo se está calculando como 1, por lo que, la solción es la siguiente:

```python
def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 0]
  return divisors

def run():
  num = int(input("Ingresa un número: "))
  print(divisores(num))

if __name__ == '__main__':
  run()
```

## Breakpoints

Los breakpoints se pueden crear en Python presionando al lado de nuestras lineas de código y marcando con un punto rojo, de esta forma, el programa de depuración se detendrá justamente cuando llegue a esa línea.