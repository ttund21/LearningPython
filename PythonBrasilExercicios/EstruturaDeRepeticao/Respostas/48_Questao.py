"""48
48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
  Exemplo:
    ```48
    12376489
    => 98467321
    ```
"""

num = int(input('Número: '))
num = str(num)
o = 0

for i in num:
    o += 1
    print(f'{num[len(num) - o]}', end='')
