"""49
49. Faça um programa que mostre os n termos da Série a seguir:
  ```49
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
  ```
  Imprima no final a soma da série.
"""

dividendo = 1
divisor = 1

n = int(input('n: '))
while True:
    m = int(input('m:'))
    if m % 2 == 0:
        continue
    else:
        break


for i in range(20):


