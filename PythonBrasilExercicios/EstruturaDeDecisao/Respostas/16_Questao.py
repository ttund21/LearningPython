# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#   Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#   Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#   Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#   Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from sys import exit
from math import sqrt

valor = []
letra = ('a', 'b', 'c')

for i in range(3):
    valor.append(float(input(f'Escrea volor de { letra[i] }: ')))

delta = (valor[1]**2) - (4 * valor[0] * valor[2])
x1 = (-(valor[1]) + sqrt(delta)) / (2 * valor[0])
x2 = (-(valor[1]) - sqrt(delta)) / (2 * valor[0])

if valor[0] == 0:
    exit('A equação não é de segundo grau.')
elif delta < 0:
    exit('A equação não possui raizes reais.')
elif delta == 0:
    exit(f'A equação possui apenas uma raiz real, x¹= { x1 } e x²= { x2 }')
else:
    exit(f'A equação possui duas raizes reais, x¹= { x1 } e x²= { x2 }')


