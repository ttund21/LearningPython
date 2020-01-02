def ilustracao():
    print('1' + '|' + '2' + '|' + '3')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('7' + '|' + '8' + '|' + '9')


def jogo(game):
    print(game[1] + '|' + game[2] + '|' + game[3])
    print('-+-+-')
    print(game[4] + '|' + game[5] + '|' + game[6])
    print('-+-+-')
    print(game[7] + '|' + game[8] + '|' + game[9])

def ganhador(game):
    from sys import exit
    # Vertical
    if game[1] == 'x' and game[4] == 'x' and game[7] == 'x' or game[1] == 'o' and game[4] == 'o' and game[7] == 'o':
        print(f'\nO {game[1]} venceu')
        exit()
    elif game[2] == 'x' and game[5] == 'x' and game[8] == 'x' or game[2] == 'o' and game[5] == 'o' and game[8] == 'o':
        print(f'\nO {game[2]} venceu')
        exit()
    elif game[3] == 'x' and game[6] == 'x' and game[9] == 'x' or game[3] == 'o' and game[6] == 'o' and game[9] == 'o':
        print(f'\nO {game[3]} venceu')
        exit()
    # Horizontal
    elif game[1] == 'x' and game[2] == 'x' and game[3] == 'x' or game[1] == 'o' and game[2] == 'o' and game[3] == 'o':
        print(f'\nO {game[1]} venceu')
        exit()
    elif game[4] == 'x' and game[5] == 'x' and game[6] == 'x' or game[4] == 'o' and game[5] == 'o' and game[6] == 'o':
        print(f'\nO {game[4]} venceu')
        exit()
    elif game[7] == 'x' and game[8] == 'x' and game[9] == 'x' or game[7] == 'o' and game[8] == 'o' and game[9] == 'o':
        print(f'\nO {game[7]} venceu')
        exit()
    # Diagonal
    elif game[1] == 'x' and game[5] == 'x' and game[9] == 'x' or game[1] == 'o' and game[5] == 'o' and game[9] == 'o':
        print(f'\nO {game[1]} venceu')
        exit()
    elif game[3] == 'x' and game[5] == 'x' and game[7] == 'x' or game[3] == 'o' and game[5] == 'o' and game[7] == 'o':
        print(f'\nO {game[3]} venceu')
        exit()

jgDaVelha = {1:' ', 2:' ', 3:' ',
        4:' ', 5:' ', 6:' ',
        7:' ', 8:' ', 9:' '}

print('Jogo Da Velha!')
ilustracao()

for i in range(9):
    while True:
        if i%2 == 0:
            try:
                jogada = int(input(f'{i + 1}º Jogada, Casa: '))
            except ValueError:
                print('Jogada de 1 a 9!')
                continue
            if jogada < 1 or jogada > 9:
                print('Jogada de 1 a 9!')
                continue
            if jgDaVelha[jogada] == 'x' or jgDaVelha[jogada] == 'o':
                print(f'Ja possui um { jgDaVelha[jogada] } nesta casa!')
                continue
            jgDaVelha[jogada] = 'x'
            jogo(jgDaVelha)
            break
        else:
            try:
                jogada = int(input(f'{i + 1}º Jogada, Casa: '))
            except ValueError:
                print('Jogada de 1 a 9!')
                continue
            if jogada < 1 or jogada > 9:
                print('Jogada de 1 a 9!')
                continue
            if jgDaVelha[jogada] == 'x' or jgDaVelha[jogada] == 'o':
                print(f'Ja possui um { jgDaVelha[jogada] } nesta casa!')
                continue
            jgDaVelha[jogada] = 'o'
            jogo(jgDaVelha)
            break
    # Resultado
    if i >= 8:
        print('\nEmpate!')
    else:
        ganhador(jgDaVelha)

