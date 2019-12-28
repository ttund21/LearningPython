# 25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = []

while True:
    addN = input('Número(Enter para finalizar): ')
    if addN == '':
        break
    else:
        n.append(float(addN))

media = sum(n) / len(n)
print(f'\nMédia: {media}\n')

if media <= 25:
    print('Turma Jovem!')
elif media <= 60:
    print('Turma Adulta!')
else:
    print('Turma Idosa!')
