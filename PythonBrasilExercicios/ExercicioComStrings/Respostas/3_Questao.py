"""3
3. Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
  F
  U
  L
  A
  N
  O
"""

nome = input('Nome: ')

for i in nome:
    print(f'{i.upper()}')
