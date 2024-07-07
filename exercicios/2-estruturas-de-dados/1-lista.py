# Crie uma lista apenas com elementos numéricos
numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = ['python', 4, [1,2,3], True, False]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(numerica[0:5])
print(mista[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(numerica[0:-1:2])

# Remova da lista o último item
print(numerica.pop())

# Insira na lista um novo item
numerica.append(15)
print(numerica)

# Remova da lista um item específico
numerica.remove(11)
print(numerica)

#----------------------#
##Manipulação de Lista
lista = ['vazia']
lista2 = numerica

lista2.extend(mista)
print(lista)
print(lista2)

mista[4] = 1.5
print(mista)
print(mista)


