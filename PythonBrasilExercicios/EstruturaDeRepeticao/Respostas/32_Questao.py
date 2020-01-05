# 32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#  Fatorial de: 5
#  5! =  5 . 4 . 3 . 2 . 1 = 120

# Função para calcular o fatorial.
def fatorial(num):
    for i in range(1, num):
        num *= i 
    print(num)

# Função para fazer a contagem regressiva.
def contador(num):
    for i in range(num, 0, -1):
        if i == 1:
            print(i, end= '')
        else:
            print(i, end = ' . ')

# Recebendo o numero.
while True:
    try:
        num = int(input('Número: '))
        break
    except ValueError:
        print('Valor Inválido!')
        continue

# Saída.
print(f'\nFatorial de: {num}')
print(f'{num}! = ', end = '')
contador(num)
print(' = ', end = '')
fatorial(num)
