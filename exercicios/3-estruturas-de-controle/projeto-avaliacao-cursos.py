# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, 
# caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos_linkedin = ['Curso de Python', 'Curso de C++', 'Curso de Go', 'Curso de JavaScript', 'Curso de Ruby']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_python = cursos_linkedin[0]
curso_javascript = cursos_linkedin[3]
curso_ruby = cursos_linkedin[4]

# 3. Crie um dicionário vazio para armazenar a nota do curso
avaliacoes = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

if curso_python in cursos_linkedin:
  print(f"O {curso_python} está na lista de cursos disponíveis.")
  avaliacoes['Python'] = int(input('Informe sua Nota: '))
if curso_javascript in cursos_linkedin:
  print(f"O {curso_javascript} está na lista de cursos disponíveis.")
  avaliacoes['JavaScript'] = int(input('Informe sua Nota: '))
if curso_ruby in cursos_linkedin:
  print(f"O {curso_ruby} está na lista de cursos disponíveis.")
  avaliacoes['Ruby'] = int(input('Informe sua Nota: '))
else:
  print('Infelizmente o curso não compõe nosso catálogo.')
  
#print(cursos_linkedin)
print(avaliacoes)



