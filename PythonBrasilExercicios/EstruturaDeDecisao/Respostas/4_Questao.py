# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

valor = input('Escreva uma letra: ')
letras = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


if valor not in letras:
    print('Consoante!')
else:
    print('Vogal')
