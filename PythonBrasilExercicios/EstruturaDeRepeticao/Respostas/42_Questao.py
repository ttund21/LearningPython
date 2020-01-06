# 42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

numeros = []
zero = 0
vinteSeis = 0
cinquentaUm = 0
setentaSeis = 0

while True:
    try:
        num = int(input('Número: '))
    except ValueError:
        print('Valor Inválido!')
        continue
    if num < 0:
        break
    else:
        numeros.append(num)

for i in numeros:
    if i >= 0 and i <= 26:
        zero += 1
    elif i >= 26 and i <= 50:
        vinteSeis += 1
    elif i >= 51 and i <= 75:
        cinquentaUm += 1
    elif i >= 76 and i <= 100:
        setentaSeis += 1
    
print(f'\n[0-25]  : {zero}\n[26-50] : {vinteSeis}\n[51-75] : {cinquentaUm}\n[76-100]: {setentaSeis}')
