# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

from sys import exit

def divi(num):
    div = []
    for i in range(2, num + 1):
        if num % i == 0:
            div.append(i)
    div.insert(0, 1)
    return print(f'Divisivel por: {div}')

try:
    num = int(input('Número: '))
except ValueError:
    exit('Só números inteiros!')


for i in range(2, num + 1):
    if num == 2 or i == num:
        print('Primo!')
        divi(num)
        break
    elif num % i == 0:
        print('Não Primo!')
        divi(num)
        break


