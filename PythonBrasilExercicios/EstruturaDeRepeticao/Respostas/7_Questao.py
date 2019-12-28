# 7. Faça um programa que leia 5 números e informe o maior número.

num = []

for i in range(5):
    num.append(float(input(f'{i + 1}º Número: ')))

print(max(num))
