def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 0]
  return divisors

def run():
  num = input("Ingresa un número: ")
  assert num.isnumeric(), "Ingresa un valor numérico"
  assert int(num) >= 0, "No puedes ingresar un número negativo"
  print(divisors(int(num)))

if __name__ == '__main__':
  run()