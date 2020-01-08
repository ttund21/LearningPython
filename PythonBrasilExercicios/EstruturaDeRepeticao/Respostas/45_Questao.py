# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#   Maior e Menor Acerto;
#   Total de Alunos que utilizaram o sistema;
#   A Média das Notas da Turma.
#  Gabarito da Prova:
#  01 - A
#  02 - B
#  03 - C
#  04 - D
#  05 - E
#  06 - E
#  07 - D
#  08 - C
#  09 - B
#  10 - A
#  Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

def compGabarito(gabarito, respostas, acertos):
    print('Comparativo de Gabarito'.center(40, '-'))
    print('Gabarito', 'Aluno'.rjust(10), '\n')
    for i in range(10):
        print(f'{gabarito[i + 1]} {respostas[i].rjust(13)}')
    print(f'Total de acertos: {acertos}')
    print(''.center(40, '-'))

def compNotas(notas, alunos):
    print('Comparativo de Notas'.center(40, '-'))
    print(f'''Maior Acerto: {max(notas)} 
Menor Acerto: {min(notas)}
Total de Alunos: {alunos}
Média de Nota da Turma: {round(sum(notas)/alunos, 2)}''')
    print(''.center(40, '-'))

def profGabarito():
    letras = ('A', 'B', 'C', 'D', 'E')
    global gabarito
    gabarito = {}
    for i in range(1, 11):
        while True:
            resposta = input(f'Resposta {i}ª Questão: ')
            if resposta.upper() not in letras:
                print('Valor Inválido!')
                continue
            else:
                break
        gabarito.setdefault(i, resposta.upper())


from random import choice

profGabarito()

respostas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letras = ('A', 'B', 'C', 'D', 'E')
notas = []
alunos = 0

while True:
    acertos = 0
    alunos += 1
    for i in range(10):
        resp = choice(letras)
        if resp == gabarito[i + 1]:
            acertos += 1
            respostas[i] = resp 
        else:
            respostas[i] = resp 
    
    notas.append(acertos)
    compGabarito(gabarito, respostas, acertos)

    proximo = input('\nTem mais aluno?(s)\n>')
    if proximo.lower() == 's':
        continue
    else:
        compNotas(notas, alunos)
        break









