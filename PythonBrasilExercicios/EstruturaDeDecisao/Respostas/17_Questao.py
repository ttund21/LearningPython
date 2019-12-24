# 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Ano: '))

mult4 = ano % 4
mult100 = ano % 100
mult400 = ano % 400

if mult4 == 0 and mult100 != 0 or mult400 == 0:
    print('Bissexto')
else:
    print('Não Bissexto')

