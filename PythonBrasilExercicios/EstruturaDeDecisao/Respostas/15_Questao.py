# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes;

lado = []

for i in range(3):
    lado.append(float(input(f'Escreva o { i + 1 }º lado: ')))

if lado[0] == lado[1] and lado[1] == lado[2]:
    print('Triângulo Equilátero')
elif lado[0] != lado[1] and lado[1] != lado[2] and lado[2] != lado[0]:
    print('Triângulo Escaleno')
else:
    print('Triângulo Isósceles')

