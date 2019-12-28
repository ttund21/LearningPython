# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = int(input('Nota de 0 a 10: '))
    if nota > 10 or nota < 0:
        print('Nota Inválida')
        continue
    else:
        break
