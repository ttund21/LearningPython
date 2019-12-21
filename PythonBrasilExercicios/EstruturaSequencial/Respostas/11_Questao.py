# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#  A. o produto do dobro do primeiro com metade do segundo .
#  B. a soma do triplo do primeiro com o terceiro.
#  C. o terceiro elevado ao cubo.

num = []

for i in range(3):
    inpNum = int(input(f'Escreva o {i + 1}º número: '))
    num.append(inpNum)

print(f'Letra A: {(2 * num[0]) + (num[1] / 2)}')
print(f'Letra B: {(3 * num[0]) + num[2]}')
print(f'Letra C: {num[2] ** 3}')
