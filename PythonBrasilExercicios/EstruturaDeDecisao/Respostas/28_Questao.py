# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#   File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#   Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#   Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

from sys import exit

def desc(valor):
    desc = valor - ((valor * 5)/100)
    return desc

carne = input('Vai levar File Duplo, Alcatra ou Picanha?\n>>> ')

if carne == 'File Duplo':
    kilos = float(input('Kilos: '))
    if kilos > 5:
        preco = kilos * 5.80
    else:
        preco = kilos * 4.90

elif carne == 'Alcatra':
    kilos = float(input('Kilos: '))
    if kilos > 5:
        preco = kilos * 6.80
    else:
        preco = kilos * 5.90

elif carne == 'Picanha':
    kilos = float(input('Kilos: '))
    if kilos > 5:
        preco = kilos * 7.80
    else:
        preco = kilos * 6.90

else:
    exit('Essa carne não existe!')

pag = input('Tipo de pagamento (D)inheiro ou (C)artão Tabajara(5% de desconto)?\n>>> ')

if pag == 'D':
    print(f'\n**Cupom Fiscal**\nCarne: {carne}\nQuantidade: {kilos}kg\nTipo de Pagamento: Dinheiro\nTotal a Pagar: R${preco}')
elif pag == 'C':
    print(f'\n**Cupom Fiscal**\nCarne: {carne}\nQuantidade: {kilos}kg\nPreço: R${preco}\nTipo de Pagamento: Cartão Tabajara\nValor do Desconto: R${round(preco - desc(preco), 2)}\nTotal a Pagar: R${desc(preco)}')
else:
    print('Tipo de pagamento inválido!')
    














