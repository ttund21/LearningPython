# 3. Faça um programa que leia e valide as seguintes informações:
#     + Nome: maior que 3 caracteres;
#     + Idade: entre 0 e 150;
#     + Salário: maior que zero;
#     + Sexo: 'f' ou 'm';
#     + Estado Civil: 's', 'c', 'v', 'd';

estCivil = ['s', 'c', 'v', 'd']

while True:
    nome = input('Nome: ')
    if len(nome) <= 3:
        print('Nome tem que ter mais de 3 caracteres!')
        continue
    else:
        break

while True:
    idade = int(input('Idade: '))
    if idade < 0 or idade > 150:
        print('Idade tem que ser entre 0 a 150!')
        continue
    else:
        break

while True:
    salario = float(input('Salário: '))
    if salario <= 0:
        print('Salário tem que ser maior que zero!')
        continue
    else:
        break

while True:
    sexo = input('Sexo: ')
    if sexo != 'f' and sexo != 'm':
        print('f - feminino e m - masculino!')
        continue
    else:
        break

while True:
    ec = input('Estado Civil: ')
    if ec not in estCivil:
        print('s - solteiro, c - casado, d - divorciado e v - viuvo!')
        continue
    else:
        break
