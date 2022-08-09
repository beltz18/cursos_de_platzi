# Crear un List comprehension de todos los multiplos de 4 que a su vez son multiplos de 6 y de 9 en un rango desde el 1 - 99999
def run():
  List = [i for i in range(1,99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
  print(List)

if __name__ == '__main__':
  run()