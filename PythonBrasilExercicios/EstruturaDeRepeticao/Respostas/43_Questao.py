# 43. O cardápio de uma lanchonete é o seguinte:
#  Especificação   Código  Preço
#  Cachorro Quente 100     R$ 1,20
#  Bauru Simples   101     R$ 1,30
#  Bauru com ovo   102     R$ 1,50
#  Hambúrguer      103     R$ 1,20
#  Cheeseburguer   104     R$ 1,30
#  Refrigerante    105     R$ 1,00
#  Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

def exibir(cod, menu, quant):
    for i in range(len(cod)):
        print(f" ")

cardapio = {100:{'nome':'Cachorro Quente', 'preco':1.20}, 101:{'nome':'Bauru Simples', 'preco':1.30}, 102:{'nome':'Bauru com ovo', 'preco':1.50}, 103:{'nome':'Hambúrger', 'preco':1.20}, 104:{'nome':'Cheeseburger', 'preco':1.30}, 105:{'nome':'Refrigerante', 'preco':1.00}}
codigo = []
quant = []

while True:
    pedido = int(input('Código(0 para encerrar): '))
    if pedido == 0:
        print('Encerrado!')
        break
    elif pedido not in cardapio:
        print('Código não está no cardápio!')
        continue
    else:
        quantidade = int(input('Quantidade: '))
        codigo.append(pedido)
        quant.append(quantidade)

exibir(codigo, cardapio, quant)
