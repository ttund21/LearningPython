# 38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#   Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#   Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#   A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

while True:
    try:
        salario = float(input('Salário: '))
        break
    except ValueError:
        print('Valor Inválido!')
        continue

porc = 1.5

for i in range(24):
    if i == 0:
        salario += ((salario * porc) / 100)
    else:
        salario += ((salario * porc) / 100) * 2

 

print(f'Salário Atual: {round(salario, 2)}')    

