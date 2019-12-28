# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

num = []

for i in range(5):
    num.append(float(input(f'{i + 1} Número: ')))

print(f'\nSoma: { sum(num) }, Média: { sum(num) / len(num) } ')
