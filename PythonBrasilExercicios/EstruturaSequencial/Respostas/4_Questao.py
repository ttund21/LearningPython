# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média
soma = 0

for i in range(4):
    print(f'Escreva {i +1}º Nota:')
    notas = float(input('>>> '))
    soma += notas

media = soma/4
print(f'Sua média anual é: {media}')
