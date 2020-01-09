#! /usr/bin/python3.7
# pw.py - Repositorio de Senha

password = {'email':'F7dsad45DfsdafasDSFGHVG4',
        'blog':'Vdsmdasd456RF.65',
        'lug':'123456789'}


import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account - copy account password]')
    sys.exit()

account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}')
