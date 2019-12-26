# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#   Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def desc(valor):
    desc = ((valor  - (valor * 10) / 100)) 
    return desc

morango = float(input('quantos kilos de Morango?\n>>> '))
maca = float(input('quantos kilos de Maçã?\n>>> '))

if morango > 5:
    valorMo = morango * 2.20
else:
    valorMo = morango * 2.50
    
if maca > 5:
    valorMa = maca * 1.50 
else:
    valorMa = maca * 1.80

if (morango + maca) > 8 or (valorMa + valorMo) > 25:
    print(f'Valor total a pagar(10% desconto): {desc(valorMo + valorMa)}')
else:
    print(f'Valor total a pagar: {valorMa + valorMo}')


