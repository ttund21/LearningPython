"""1
1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
  Compara duas strings
  String 1: Brasil Hexa 2006
  String 2: Brasil! Hexa 2006!
  Tamanho de "Brasil Hexa 2006": 16 caracteres
  Tamanho de "Brasil! Hexa 2006!": 18 caracteres
  As duas strings são de tamanhos diferentes.
  As duas strings possuem conteúdo diferente.
"""

def tamanho(strings):
    for i in range(2):
        print(f'Tamanho de "{strings[i]}": { len(strings[i]) } caracteres ')

def comparacao(strings):
    for i, j in zip(range(len(strings) - 1), range(1, len(strings))):
        if len(strings[i]) == len(strings[j]):
            print('As duas strings são de tamanhos iguais.')
        else:
            print('As duas strings são de tamanhos diferentes.')
        if strings[i] == strings[j]:
            print('As duas strings possuem conteúdo iguais.')
        else:
            print('As duas strings possuem conteúdo diferente.')

strings = []

for i in range(2):
    s = input(f'{i + 1}ª String: ')
    strings.append(s)

tamanho(strings)
comparacao(strings)
