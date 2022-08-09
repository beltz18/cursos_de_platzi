# Crear un dictionary comprehension que guarde los primeros 1000 números naturales con sus raíces cuadradas como valores
from math import sqrt

def run():
  Dict = {i: sqrt(i) for i in range(1,1001)}
  print(Dict)

if __name__ == '__main__':
  run()