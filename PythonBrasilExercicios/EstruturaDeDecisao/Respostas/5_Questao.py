# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menor do que sete;
#   A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota = []

for i in range(2):
    addNota = float(input(f'{i + 1}º Nota: '))
    nota.append(addNota)

media = (nota[0] + nota[1]) / 2

if media == 10:
    print('Aprovado com distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
