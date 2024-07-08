# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
fase_atual = 1
fase_final = 5

# Crie um while loop que imprima na tela o nível atual
##while fase_atual <= fase_final:
##  print(f'Nivel Atual: {fase_atual}')
##  fase_atual += 1

# Insira "else" no while loop anterior.
while fase_atual <= fase_final:
  print(f'Nivel Atual: {fase_atual}')
  fase_atual += 1
else:
  print('Fase final concluída!')