def run():
  # MANERA TRADICIONAL:
  # List = list()
  # for i in range(1,11):
  #   if i % 3 != 0 :
  #     List.append(i**2)

  # CON LIST COMPREHENSIONS
  # element for element in iterable if condition
  List = [i**2 for i in range(1,11) if i % 3 != 0] # el if es opcional
  print(List)

if __name__ == '__main__':
  run()