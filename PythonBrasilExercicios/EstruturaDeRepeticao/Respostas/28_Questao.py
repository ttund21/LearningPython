# 28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

valorCD = []
numCD = int(input('Número de CDs: '))

for i in range(numCD):
    while True:
        precoCD = float(input(f'Preço do {i + 1}º CD?\n>>> '))
        if precoCD < 0:
            print('Valor Inválido!')
            continue
        else:
            valorCD.append(precoCD)
            break

print(f'O valor médio gasto é de: { sum(valorCD) / len(valorCD)  }')
