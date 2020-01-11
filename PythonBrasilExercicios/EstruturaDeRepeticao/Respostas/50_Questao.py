# 50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

divisor = 1
resultado = 0
exibir = []

while True:
    try:
        n = int(input('N = '))
        break
    except ValueError:
        print('Valor Inválido!')
        continue

while divisor <= n:
    exibir.append('1' + '/' + str(divisor))
    resultado += (1 / divisor)
    divisor += 1

print(f"H = {' + '.join(exibir)}\nH = { round(resultado, 2) }")
