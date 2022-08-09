def run():
  # Lista y diccionario normales
  myList = [1, "hello", 4.5]
  myDict = {"fname": "Beltz", "lname": "A"}

  # Lista de diccionarios y diccionario de listas
  superList = [
    {
      "city": "New York",
      "country": "EEUU"
    },
    {
      "city": "Caracas",
      "country": "Venezuela"
    }
  ]
  superDict = {
    "integer_nums": [0,1,2,3,4,5,6,7,8,9],
    "float_nums": [0.1,0.2,0.3,0.4,0.5]
  }

  print(myList,myDict)
  
  for key,value in superDict.items():
    print(key, "-", value)
  for index in superList:
    print(index)

# Entry point
# Inicia la función apenas se ejecute el archivo de Python pero a su vez determina si se está ejecutando en la terminal
if __name__ == '__main__':
  run()