# 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

num = []

for i in range(2):
    num.append(float(input(f'{i + 1}º Número: ')))

oper = input('Qual operação vc quer usar? +, -, /, *\n>>> ')

if oper == '+':
    result = num[0] + num[1]
elif oper == '-':
    result = num[0] - num[1]
elif oper == '/':
    result = num[0] / num[1]
elif oper == '*':
    result = num[0] * num[1]
else:
    print('Comando Inválido!')

print(f'\nResultado = {result}')
if result < 0:
    print('Negativo')
else:
    print('Positivo')

if round(result) != result:
    print('Decimal')
else:
    print('Inteiro')
    if result % 2 == 0:
        print('Par')
    else:
        print('Impar')
