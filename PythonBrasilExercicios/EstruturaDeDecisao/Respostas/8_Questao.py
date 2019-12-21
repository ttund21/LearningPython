# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco = []

for i in range(3):
    addPreco = float(input(f'Add o {i + 1}º preço: '))
    preco.append(addPreco)

print(f'Você de comprar o produto que custa: { min(preco) }')
