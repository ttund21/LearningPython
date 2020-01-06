# 41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#  Os juros e a quantidade de parcelas seguem a tabela abaixo:
#  Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#  1       0
#  3       10
#  6       15
#  9       20
#  12      25
#  Exemplo de saída do programa:
#  Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#  R$ 1.000,00     0               1                       R$  1.000,00
#  R$ 1.100,00     100             3                       R$    366,00
#  R$ 1.150,00     150             6                       R$    191,67

parcela = (1, 3, 6, 9, 12)
juro = (0, 10, 15, 20, 25)

while True:
    try:
        divida = float(input('Valor da divida: '))
    except ValueError:
        print('Valor Inválida!')
        continue

print('Valor da Dívida | Valor do Juros | Quantidade de Parcelas | Valor da Parcela')
for i in parcela:
    diferenca = (divida * juro[parcela.index(i)]) / 100
    juros = juro[parcela.index(i)]
    if juros == 0:
        print(f'R$ { divida  + diferenca }                { juros }              { i }                     R$ { divida  + diferenca }')
    else:
        print(f'R$ { divida  + diferenca }                { juros }             { i }                     R$ { round((divida  + diferenca) / i, 2) }')
