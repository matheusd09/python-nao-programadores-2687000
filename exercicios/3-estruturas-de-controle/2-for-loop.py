# Crie uma lista
lista = ['Curso de Python', 'Curso de C++', 'Curso de Go', 'Curso de JavaScript', 'Curso de Ruby']

# Crie um for loop para imprimir cada elemento dessa lista
for n in lista:
  print(n)
  

# Crie um objeto iterável utilizando a função range()
range(5)
list(range(5))
list(range(30,40,2))


# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
##for n in range(7):
for item in range(2,7):
  print(f'{item} - Estou aprendendo Python')
else:
  print('Fim do Loop')
