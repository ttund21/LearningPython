# 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Número: '))

for i in range(2, num + 1):
    if num == 2 or num == i:
        print('Primo!')
        break
    elif num % i == 0:
        print('Não Primo!')
        break
