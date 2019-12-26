# 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#   Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#   Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input('Valor do Saque: '))

if saque >= 10 and saque <= 600:
    nota100 = saque // 100
    nota50 = (-(nota100 * 100) + saque) // 50 
    nota10 = (-(nota100 * 100) - (nota50 * 50) + saque) // 10
    nota5 = (-(nota100 * 100) - (nota50 * 50) - (nota10 * 10) + saque) // 5
    nota1 = (-(nota100 * 100) - (nota50 * 50) - (nota10 * 10) - (nota5 * 5) + saque) // 1
    print(f'Para sacar { saque } reais, o programa fornece {nota100} de cem, {nota50} de cinquenta, {nota10} de dez, {nota5} de cinco e {nota1} de um. ')
else:
    print('Valor Inválido!')
