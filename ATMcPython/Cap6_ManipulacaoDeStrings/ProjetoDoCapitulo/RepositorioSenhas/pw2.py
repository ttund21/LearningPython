#! /usr/bin/python3.7

import sys, pyperclip

passwords = {}

if len(sys.argv) < 2:
    print('Falta de argumentos!')
elif sys.argv[1] == 'add':
    account = input('Conta: ')
    pw = input('Senha: ')
    if account not in passwords.keys():
        passwords.setdefault(account, pw)
    else:
        passwords[account] = pw
elif sys.argv[1] in passwords:
    pyperclip.copy[passwords[sys.argv[1]]]
    print('Copiado!')
else:
    print('Comando Inválido')
