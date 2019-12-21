# 1. Faça um Programa que peça dois números e imprima o maior deles.

num = []

for i in range(2):
    addNum = int(input('Add numero: '))
    num.append(addNum)

print(f'O número maior é: {max(num)}')
