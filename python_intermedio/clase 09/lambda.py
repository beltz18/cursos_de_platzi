# Recibe un valor de tipo cadena, lo pone de revés y valída si es igual a la cadena original
palindrome = lambda string: string == string[::-1]
print(palindrome('ana'))