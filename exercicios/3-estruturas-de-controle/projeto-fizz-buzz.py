# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# 2. Crie um for loop para percorrer todos os elementos da lista
##for n in lista1:

# 3. Crie uma estrutura condicional para verificar cada número da lista:
##if n in lista1:

# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"

lista_numerica = list(range(10,31))
indice = 0
print(lista_numerica)

for n in lista_numerica:
  if (n % 5 == 0) and (n % 3 == 0):
    lista_numerica[indice] = 'FizzBuzz'
  elif n % 3 == 0:
    lista_numerica[indice] = 'Fizz'
  elif n % 5 == 0:
    lista_numerica[indice] = 'Buzz'
  else:
    lista_numerica[indice] = n
  indice += 1

print(lista_numerica)




