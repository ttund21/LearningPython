# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

from datetime import date
from sys import exit

try:
    data = date(int(input('Ano: ')), int(input('Mês: ')), int(input('Dia: ')))
except:
    exit('Data Inválida!')
print(f'Essa { data } é válida!')
