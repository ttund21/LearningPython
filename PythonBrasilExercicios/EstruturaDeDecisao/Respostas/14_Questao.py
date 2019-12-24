# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media <= 4:
        mediaFinal = 'E'
    elif media <= 6:
        mediaFinal = 'D'
    elif media <= 7.5:
        mediaFinal = 'C'
    elif media <= 9:
        mediaFinal = 'B'
    else:
        mediaFinal = 'A'

    return mediaFinal

aprovado = ('A', 'B', 'C')
notaGeral = media(float(input('Primeira Nota: ')), \
        float(input('Segunda Nota: ')))

if notaGeral in aprovado:
    print(f'Sua nota foi { notaGeral }, Aprovado')
else:
    print(f'Sua nota foi { notaGeral }, Reprovado')
