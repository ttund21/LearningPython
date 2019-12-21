# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

valor = input('Escreva F ou M: ')

if valor == 'F':
    print('Feminino')
elif valor == 'M':
    print('Masculino')
else:
    print('Sexo Inválido')
