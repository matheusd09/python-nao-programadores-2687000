ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade_formatura = ano_formatura - ano_nascimento
print(f'Gerlaine possuía {idade_formatura} anos quando formou.')

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
a = 2
b = 50
b > a   # True
b >= a  # True
b <= a   # False
b == a   # False
'python' != 'javascript' # True (compara o comprimento da string)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
3 == 3 and 2 == 2 #True
3 == 3 and 2 == 1 #False
3 == 3 or 2 == 2  #True
3 == 3 or 2 == 1  #True
not 3 == 1        #True
not 3 == 3        #False
