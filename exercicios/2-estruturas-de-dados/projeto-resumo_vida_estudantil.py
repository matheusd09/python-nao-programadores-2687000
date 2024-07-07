# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e 
# os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}

estudante['nome'] = input('Informe seu nome: ')
estudante['ano_linkedin'] = int(input('Em qual ano você conheceu o Linkedin? '))
estudante['ano_atual'] = int(input('Informe o ano atual: '))
cursos = input('Quais cursos do LinkedIn Learning você já fez? (Separados por virgula) ')
estudante['cursos'] = cursos.split(', ')

# 2. Armazene esses dados em um dicionário


# 3. Imprima na tela uma string com as informações de 
# nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

total_anos = estudante['ano_atual'] - estudante['ano_linkedin']
total_cursos = len(estudante['cursos'])

print(f"Olá {estudante['nome']}, você conheceu o linkedin em {estudante['ano_linkedin']}, e desde então se passaram {total_anos} anos.\
      \nNesse periodo, você realizou {total_cursos} cursos. Sendo o primeiro: {estudante['cursos'][0]}, e o mais recente: {estudante['cursos'][-1]}.")

