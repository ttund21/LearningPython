# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    user = input('Usuário: ')
    senha = input('Senha: ')
    if user == senha:
        print('Erro usuário e senha não podem ser iguais.')
        continue
    else:
        break

