# 43. O cardápio de uma lanchonete é o seguinte:
#  Especificação   Código  Preço
#  Cachorro Quente 100     R$ 1,20
#  Bauru Simples   101     R$ 1,30
#  Bauru com ovo   102     R$ 1,50
#  Hambúrguer      103     R$ 1,20
#  Cheeseburguer   104     R$ 1,30
#  Refrigerante    105     R$ 1,00
#  Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

def exibir(carrinho, cardapio):
    total = []
    print('\n')
    print('Carrinho'.center(40, '-'))
    for codigo in carrinho:
        print(f" { cardapio[codigo]['nome'] }(R${ cardapio[codigo]['preco'] }) X { carrinho[codigo] } = R$ { round(cardapio[codigo]['preco'] * carrinho[codigo], 2) }  ")
        total.append(round(cardapio[codigo]['preco'] * carrinho[codigo], 2))
    print('\n')
    print('Total'.center(40, '-'))
    print(f" Total a ser pago: R$ { sum(total) }")
    print(''.center(40, '-'))

def menu():
    print('Menu'.center(40, '-'))
    print('''Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00''')
    print(''.center(40, '-'))


cardapio = {100:{'nome':'Cachorro Quente', 'preco':1.20}, 101:{'nome':'Bauru Simples', 'preco':1.30}, 102:{'nome':'Bauru com ovo', 'preco':1.50}, 103:{'nome':'Hambúrger', 'preco':1.20}, 104:{'nome':'Cheeseburger', 'preco':1.30}, 105:{'nome':'Refrigerante', 'preco':1.00}}
carrinho = {}

menu()

print('\n')
print('Pedido'.center(40, '-'))
while True:
    try:
        pedido = int(input('Código(0 para encerrar): '))
        if pedido == 0:
            print('Encerrado!')
            print(''.center(40, '-'))
            break
        elif pedido not in cardapio:
            print('Código não está no cardápio!')
            continue
        else:
            quantidade = int(input('Quantidade: '))
            carrinho.setdefault(pedido, quantidade)
    except ValueError:
        print('Valor Inválido!')
        continue

exibir(carrinho, cardapio)
