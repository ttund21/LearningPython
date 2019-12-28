# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = []

while True:
    addN = input('Número(Enter para parar): ')
    if addN == '':
        break
    else:
        n.append(float(addN))

print(f'Máximo: { max(n) }, Minimo: { min(n) }')
