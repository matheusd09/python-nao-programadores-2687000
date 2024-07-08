# Declare 4 variáveis do tipo numérica
num1 = 1
num2 = 2
num3 = 3
num4 = 4

# Crie uma estrutura condicional para comparar dois números
if num1 == num2:
  print(f'Condição Verdadeira, o numero {num1} é igual ao numero {num2}')
else:
  print(f'Condição Falsa, o numero {num1} é diferente do numero {num2}')

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if num3 > num2:
  print(f'Condição Verdadeira, o numero maior é o {num3}')


# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if num1 > num2:
  print(f'Condição Verdadeira, o numero maior é o {num1}')
else:
  print(f'Condição Falsa, o numero maior é o {num2}')

# Insira outras condições na estrutura condicional usando o elif
if num1 > num2:
  print(f'Condição Verdadeira, o numero {num1} é maior que o numero {num2}')
elif num1 > num3:
  print(f'Nesse caso, o numero {num1} é maior que o numero {num3}')
else:
  print(f'Condição Falsa, o numero maior é o {num3}')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (num1 > num2) or (num1 > num3):
  print(f'{num1} é maior que {num2} ou maior que o {num3}.')
elif (num3 == num4) and (num5 > num4):
  print(f'Nesse caso, o numero {num3} é igual ao {num4} e o {num5} é maior que o {num4}.')
else:
  print('Nenhuma das condições são verdadeiras')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if num1 < num2:
   print(f'O {num1} é menor que {num2}.')
if num3 > num2:
  print(f'O {num3} é maior que {num2}.')