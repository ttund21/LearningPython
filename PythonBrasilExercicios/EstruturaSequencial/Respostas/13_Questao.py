# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#  + Para homens: (72.7*h) - 58
#  + Para mulheres: (62.1*h) - 44.7

print('Calculadora de peso ideal')
sexo = input('Qual seu sexo? M ou F ')
altura = float(input('Qual sua Altura? '))

if sexo == 'M' or sexo == 'm':
    print(f'Seu peso ideal é: { (72.7 * altura) - 58 }')
elif sexo == 'F' or sexo == 'f':
    print(f'Seu peso ideal é: { (62.1 * altura) - 44.7 }')
else:
    print('Comando Invalido!')

