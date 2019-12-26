# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = input('Número: ')

if '.' in num or ',' in num:
    print('Decimal!')
else:
    print('Inteiro')
