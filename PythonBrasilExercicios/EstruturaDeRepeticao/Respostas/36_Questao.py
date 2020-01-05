# 36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#  Montar a tabuada de: 5
#  Começar por: 4
#  Terminar em: 7
#  Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#  5 X 4 = 20
#  5 X 5 = 25
#  5 X 6 = 30
#  5 X 7 = 35
#  Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

while True:
    try:
        num = int(input('Número: '))
        break
    except ValueError:
        print('Valor Inválido!')
        continue

while True:
    try:
        inicio = int(input('Inicio: '))
        fim = int(input('Final: '))
    except ValueError:
        print('Valor Inválido!')
        continue
    if inicio > fim:
        print('Inicio tem que ser menor que o final.')
        continue
    else:
        break

for i in range(inicio, fim + 1):
    print(f'{num} X {i} = { num * i }')

