# 27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

alunos = []
turmas = int(input('Número de turmas: '))

for i in range(turmas):
    while True:
        numAlunos = int(input(f'Número de alunos da {i + 1}º turma?\n>>> '))
        if numAlunos >= 0 and numAlunos <= 40:
            alunos.append(numAlunos)
            break
        else:
            print('Números de alunos não pode ser menor que 0 ou maior que 40.')

print(f'A média de alunos por turma é: { sum(alunos) / len(alunos)  }')
