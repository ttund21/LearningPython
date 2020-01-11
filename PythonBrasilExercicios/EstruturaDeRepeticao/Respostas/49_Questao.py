"""49
49. Faça um programa que mostre os n termos da Série a seguir:
  ```49
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
  ```
  Imprima no final a soma da série.
"""

dividendo = 1
divisor = 1
resultado = 0
exibir = []

while True:
    try:
        n = int(input('n: '))
        break
    except ValueError:
        print('Valor Inválido')
        continue

while True:
    try:
        m = int(input('m: '))
    except ValueError:
        print('Valor Inválido')
        continue
    if m % 2 == 0 or m < n:
        continue
    else:
        break


while dividendo <= n and divisor <= m:
    exibir.append(str(dividendo) + '/' + str(divisor))
    resultado += dividendo/divisor
    dividendo += 1
    divisor += 2

print(f"S = {' + '.join(exibir)}\nS = {round(resultado, 2)} ")

