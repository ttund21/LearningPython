# 34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input('Número: '))

for i in range(2, num + 1):
    if i == num:
        print('Primo')
        break
    elif num % i == 0:
        print('Não Primo')
        break
