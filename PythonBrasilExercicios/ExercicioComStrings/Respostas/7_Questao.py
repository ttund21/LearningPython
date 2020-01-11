"""7
7. Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

  + quantos espaços em branco existem na frase.
  + quantas vezes aparecem as vogais a, e, i, o, u.

"""

vogais = ('a', 'e', 'i', 'o', 'u')
numBranco = 0
numVogais = 0

frase = input('Frase: ')

for i in frase:
    if i == ' ':
        numBranco += 1
    if i in vogais:
        numVogais += 1

print(f'''\nNúmero de espaços em branco: {numBranco}
Número de vogais: {numVogais}''')
