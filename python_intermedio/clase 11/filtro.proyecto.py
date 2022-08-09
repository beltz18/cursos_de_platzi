from Data.data import DATA

filtro = input("Lenguaje a filtrar: ")

def run():
  ### All Language Workers Filter
  ## With comprehensions:
  # all_language_workers = [worker for worker in DATA if filtro in worker['languages']]
  ## With high order functions:
  all_language_workers = list(filter(lambda worker: filtro in worker['languages'], DATA))
  all_language_workers = list(map(lambda worker: worker, all_language_workers))

  ### Overage or Underage Workers
  ## With high order functions:
  # adults = list(filter(lambda worker: worker['age'] >= 18, DATA))
  # adults = list(map(lambda worker: worker['first_name'], adults))
  ## With list comprehensions:
  adults = [worker['first_name'] for worker in DATA if worker['age'] >= 18]
  
  if all_language_workers:
    print(f'\nTrabajadores que son expertos en {filtro}:')

    if len(DATA) == len(adults):
      for worker in all_language_workers:
        print('* {} {}'.format(worker['first_name'], worker['last_name']))
      print("Todos los trabajadores son mayores de edad")
    else:
      for worker in all_language_workers:
        if worker['first_name'] in adults: msg = "Mayor de edad"
        else: msg = "Menor de edad"
        print('* {} {} - [{}]'.format(worker['first_name'], worker['last_name'], msg))
  else:
    print(f'No hay trabajadores que sean expertos en {filtro} :(')

if __name__ == '__main__':
  run()