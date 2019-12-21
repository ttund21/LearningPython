# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#  + salário bruto.
#  + quanto pagou ao INSS.
#  + quanto pagou ao sindicato.
#  + o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#  + Salário Bruto : R$
#  - IR (11%) : R$
#  - INSS (8%) : R$
#  - Sindicato ( 5%) : R$
#  = Salário Liquido : R$
#  Obs.: Salário Bruto - Descontos = Salário Líquido.

print('Calculadora de salário liquido')
sHora = float(input('Quanto você ganha por hora? '))
horaMes = float(input('Quantas horas você trabalha por mês? '))
sBruto = sHora * horaMes
ir = (sBruto * 11) / 100
inss = (sBruto * 8) / 100
sind = (sBruto * 5) / 100
sLiquido = sBruto - ir - inss - sind

print(f'Seu salário bruto: R${ sBruto }')
print(f'Você pagou R${ ir } de IR')
print(f'Você pagou R${ inss } de INSS')
print(f'Você pagou R${ sind } para o Sindicato')
print(f'Seu salário liquido é de R${ sLiquido }')




