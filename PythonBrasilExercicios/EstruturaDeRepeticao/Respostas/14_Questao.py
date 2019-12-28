# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

num = []
par = []
impar = []


for i in range(10):
    num.append(float(input(f'{i + 1}º Número: ')))

print(f'Soma: { sum(num) }')

for i in num:
    if (i % 2) == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Soma: { sum(num) }, Qtd de nº Pares: { len(par) } e Qtd de nº Ímpares: { len(impar) }')
        


