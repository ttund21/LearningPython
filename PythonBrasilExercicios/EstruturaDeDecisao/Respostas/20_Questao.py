# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#   A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#   A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#   A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota = []

for i in range(3):
    nota.append(float(input(f'{ i + 1 }º Nota: ')))

media = sum(nota) / len(nota)

if media >= 7:
    print('Aprovado!')
elif media < 7:
    print('Rerovado!')
else:
    print('Aprovado com distinção!')

