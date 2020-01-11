# 9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

# Ps: Ainda não sei usar regex.

def validador(cpf):
    if len(cpf) < 14:
        return False

    for i in range(3):
        if not cpf[i].isdecimal():
            return False

    if cpf[3] != '.':
        return False

    for i in range(4, 7):
        if not cpf[i].isdecimal():
            return False

    if cpf[7] != '.':
        return False

    for i in range(8, 11):
        if not cpf[i].isdecimal():
            return False

    if cpf[11] != '-':
        return False

    for i in range(12, 14):
        if not cpf[i].isdecimal():
            return False

    return True



cpf = input('CPF: ')

if validador(cpf):
    print('CPF válido!')
else:
    print('Inválido!')



