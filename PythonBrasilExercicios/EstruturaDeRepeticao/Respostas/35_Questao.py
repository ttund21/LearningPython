# 35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

def primo(num):
    for i in range(2, num + 1):
        if i == num:
            print(num, end = ' ')
        elif num % i == 0:
            break

num = int(input('Número: '))

for i in range(1, num + 1):
    primo(i)

