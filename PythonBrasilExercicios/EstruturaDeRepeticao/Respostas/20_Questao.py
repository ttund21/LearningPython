# 20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16

while True:
    fatorial = 1
    try:
        num = int(input('Número: '))
    except ValueError:
        break
    if num > 16 or num < 0:
        break
    else:
        for i in range(1, num + 1):
            fatorial *= i

    print(fatorial)
