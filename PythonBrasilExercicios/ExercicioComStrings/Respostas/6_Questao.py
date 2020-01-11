"""6
6. Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
  Data de Nascimento: 29/10/1973
  Você nasceu em  29 de Outubro de 1973.
"""

mes = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}

while True:
    try:
        dd = int(input('Dia(dd/mm/aaaa): '))
        if dd <= 0:
            print('Valor Inválido!')
            continue
        mm = int(input(f'Mês({dd}/mm/aaaa): '))
        if mm <= 0:
            print('Valor Inválido!')
            continue
        aaaa = int(input(f'Ano({dd}/{mm}/aaaa): '))
        if aaaa <= 0:
            print('Valor Inválido!')
            continue
        break
    except ValueError:
        print('Valor Inválido!')
        continue

print(f'\nData de Nascimento: {dd}/{mm}/{aaaa}')
print(f'Você nasceu em {dd} de {mes[mm]} de {aaaa}.')
