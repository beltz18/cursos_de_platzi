def read():
  names = []
  with open('./data.txt', 'r', encoding='utf-8') as file:
    for line in file:
      names.append(line)
  print(names)

def write():
  names = ['Andi', 'José', 'Yulieth', 'Nelson', 'Joshua']
  with open('./data.txt', 'w', encoding='utf-8') as file:
    for name in names:
      file.write(name)
      file.write('\n')

def append():
  names = ['Andi', 'José', 'Yulieth', 'Nelson', 'Joshua']
  with open('./data.txt', 'a', encoding='utf-8') as file:
    for name in names:
      file.write(name)
      file.write('\n')

def run(fun):
  fun()

if __name__ == '__main__':
  run(write)