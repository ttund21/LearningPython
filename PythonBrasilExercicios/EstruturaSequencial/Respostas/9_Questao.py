# 9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

print('Converor de Farenheit para Celsius')
faren = float(input('Farenheit: '))
print(f'{faren} em celsius é {(5 * (faren - 32) / 9)}.')
