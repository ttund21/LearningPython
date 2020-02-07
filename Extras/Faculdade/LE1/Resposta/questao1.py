from random import randint

# Gerador de números aleatorios para lista.
def listGenerator(tam, lista):
    for i in range(tam):
        lista.append(randint(0,100))

# Variáveis
lista1 = []
lista2 = []

# Coletar a quantidade de itens da lista
while True:
    try:
        lenLista1 = int(input("Tamanho da lista 1: "))
        lenLista2 = int(input("Tamanho da lista 2: "))
        break
    except ValueError:
        print("valor Inválido!")
        continue

# Populando as listas.
listGenerator(lenLista1, lista1)
listGenerator(lenLista2, lista2)

# Criando a lista três com os itens da 1 e 2.
lista3 = lista1 + lista2


while True:
    print(f"\n\nLista 1: {lista1}\nLista 2: {lista2}\nLista 3: {lista3}\n")

    try:
        escolha = int(input('''(1) Inserir um número aleatório na lista 3
(2) Remover o último número da lista 3
(3) Imprimir a soma dos números da lista 3
(4) Imprimir a quantidade de números existentes nas listas 1, 2 e 3
(5) Imprimir as três listas em ordem crescente
(0) Finalzar programa
>>> '''))
    except ValueError:
        print('Valor Inválido!')
        continue
    if escolha == 1:
        lista3.append(randint(0,100))
        print("Valor aleátorio adicionado na lista!")
    elif escolha == 2:
        del lista3[len(lista3) - 1]
        print("Último valor da lista 3 apagado!")
    elif escolha == 3:
        print(f"Soma dos números da lista 3: {sum(lista3)}.")
    elif escolha == 4:
        print(f"Quantidades de números existentes:\nLista 1: {len(lista1)}\nLista 2: {len(lista2)}\nLista 3: {len(lista3)}")
    elif escolha == 5:
        print(f"Lista em ordem crescentes:\nLista 1: {sorted(lista1)}\nLista 2: {sorted(lista2)}\nLista 3: {sorted(lista3)}")
    elif escolha == 0:
        print('Finalizado!')
        break
    else:
        print('Comando Inválido!')
