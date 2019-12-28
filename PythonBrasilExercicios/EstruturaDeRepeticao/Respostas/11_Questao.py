# 11. Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
soma = 0

for i in range(num1 + 1, num2):
    soma += i
    print(i, end=' ')

print(f'\nSoma: {soma}')

