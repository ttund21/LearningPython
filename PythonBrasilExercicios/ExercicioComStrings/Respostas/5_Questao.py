"""5
5. Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
  FULANO
  FULAN
  FULA
  FUL
  FU
  F
"""

nome = input('Nome: ')

for i in range(len(nome)):
    print(f'{nome[0:len(nome) - i].upper()}')

