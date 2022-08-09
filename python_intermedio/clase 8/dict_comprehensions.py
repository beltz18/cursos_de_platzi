def run():
  # MANERA TRADICIONAL
  # Dict = dict()
  # for i in range(1,11):
  #   if i % 3 != 0:
  #     Dict[i] = i**3

  # CON DICT COMPREHENSIONS
  Dict = {i: i**3 for i in range(1,11) if i % 3 != 0}
  print(Dict)

if __name__ == '__main__':
  run()