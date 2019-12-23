# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 280,00 (incluindo) : aumento de 20%
#   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#   salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#       o salário antes do reajuste;
#       o percentual de aumento aplicado;
#       o valor do aumento;
#       o novo salário, após o aumento.

salario = float(input('Qual o seu salário?\n>>> R$'))

if salario < 280:
    aumento = (salario * 20) / 100
    print(f'Seu salário atual é de { salario }.')
    print(f'Será aplicado um aumento de 20%, R${ aumento }.')
    print(f'Seu novo salário é de: R${ salario + aumento }')
elif salario >= 280 and salario < 700:
    aumento = (salario * 15) / 100
    print(f'Seu salário atual é de { salario }.')
    print(f'Será aplicado um aumento de 15%, R${ aumento }.')
    print(f'Seu novo salário é de: R${ salario + aumento }')
elif salario >= 700 and salario < 1500 :
    aumento = (salario * 10) / 100
    print(f'Seu salário atual é de { salario }.')
    print(f'Será aplicado um aumento de 10%, R${ aumento }.')
    print(f'Seu novo salário é de: R${ salario + aumento }')
else:
    aumento = (salario * 5) / 100
    print(f'Seu salário atual é de { salario }.')
    print(f'Será aplicado um aumento de 5%, R${ aumento }.')
    print(f'Seu novo salário é de: R${ salario + aumento }')


