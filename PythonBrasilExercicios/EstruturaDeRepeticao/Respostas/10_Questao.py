# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Número 1:'))
num2 = int(input('Número 2:'))

for i in range(num1 + 1, num2):
    print(i)
