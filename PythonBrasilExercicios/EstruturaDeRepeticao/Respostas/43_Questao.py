# 43. O cardápio de uma lanchonete é o seguinte:
#  Especificação   Código  Preço
#  Cachorro Quente 100     R$ 1,20
#  Bauru Simples   101     R$ 1,30
#  Bauru com ovo   102     R$ 1,50
#  Hambúrguer      103     R$ 1,20
#  Cheeseburguer   104     R$ 1,30
#  Refrigerante    105     R$ 1,00
#  Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio = {100:1.20, 101:1.30, 102:1.50, 103:1.20, 104:1.30, 105:1.0}
carrinho = []

while True:
    pedido = int(input('Código(0 para encerrar): '))
    if pedido == 0:
        print('Encerrado!')
        break
    quantidade = int(input('Quantidade: '))
    carrinho.append(cardapio[pedido] * quantidade)

print(f'Código ')



