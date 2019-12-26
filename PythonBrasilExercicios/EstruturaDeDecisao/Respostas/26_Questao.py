# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   Álcool:
#   até 20 litros, desconto de 3% por litro
#   acima de 20 litros, desconto de 5% por litro
#   Gasolina:
#   até 20 litros, desconto de 4% por litro
#   acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

alcGas = input('Vai querer álcool ou gasolina? Escreva A para álcool e G paragasolina\n>>> ')
litro = 0

if alcGas == 'A' or alcGas == 'G':
    litro = float(input('Vai abastecer quantos litros?\n>>> '))
    if alcGas == 'A':
        if litro <= 20:
            litro *= 1.90
            litro = litro - (litro * 3) /100
            print(f'Preço: R${litro}')
        else:
            litro *= 1.90
            litro = litro - (litro * 5) / 100
            print(f'Preço: R${litro}')
    if alcGas == 'G':
        if litro <= 20:
            litro *= 2.50
            litro = litro - (litro * 4) /100
            print(f'Preço: R${litro}')
        else:
            litro *= 2.50
            litro = litro - (litro * 6) / 100
            print(f'Preço: R${litro}')
else:
    print('Comando Inválido')


        
                

                

