# 24. Faça um programa que calcule o mostre a média aritmética de N notas.

n = []

while True:
    addN = input('Número(Enter para finalizar): ')
    if addN == '':
        break
    else:
        n.append(float(addN))

print(f'\nMédia: { sum(n) / len(n) }')

