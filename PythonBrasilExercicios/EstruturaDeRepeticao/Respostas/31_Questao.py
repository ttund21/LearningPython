# 31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#  Lojas Tabajara
#  Produto 1: R$ 2.20
#  Produto 2: R$ 5.80
#  Produto 3: R$ 0
#  Total: R$ 8.00
#  Dinheiro: R$ 20.00
#  Troco: R$ 12.00
#  ...

while True:
    produto = []

    # Captando os valores dos produtos.
    while True:
        try:
            preco = float(input('Preço(0 para finalizar): '))
        except ValueError:
            print('Valor Inválido!')
            continue
        if preco == 0:
            break
        else:
            produto.append(preco)

    print(f'Total: R$ {sum(produto)}')

    # Gerando o valor total do produto, captando o dinheiro e gerando o troco.
    while True:
        try:
            dinheiro = float(input('Dinheiro: '))
        except ValueError:
            print('Valor Inválido!')
            continue
        if dinheiro < sum(produto):
            print('Saldo Inválido!')
            continue
        else:
            troco = dinheiro - sum(produto)
            break
    
    # Gerando saída.
    print('\nLojas Tabajara')
    for i in range(len(produto)):
        print(f'Produto {i + 1}: R$ {produto[i]}')
    print(f'Total: R$ {sum(produto)}\nDinheiro: R$ {dinheiro}\nTroco: R$ {troco}\n...\n')
