def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 0]
  return divisors

def run():
  try:
    num = int(input("Ingresa un número: "))
    if num < 0:
      raise ValueError("El número no puede ser negativo")
    print(divisors(num))
  except ValueError as ve:
    print(ve)

if __name__ == '__main__':
  run()