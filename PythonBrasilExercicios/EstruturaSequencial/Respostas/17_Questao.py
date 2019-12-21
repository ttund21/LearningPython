# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#  + comprar apenas latas de 18 litros;
#  + comprar apenas galões de 3,6 litros;
#  + misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil # ceil é usado para arredondar um número para cima.

print('Calculadora de preço de tinta') # Esse parte vai capturar as informações
area = float(input('Area em m² a ser pintada: '))
opcCompra = input('1 - Para comprar apenas latas;\n2 - Para comprar apenas galões;\n3 - Para misturar.\n>>> ')

if opcCompra == '1':
    refil = area/108 # Aqui vai calcular quantidade de refil(latas) a serem utilizadas, 18 litros(Uma lata) pinta 108 m²(Regra de 3). 
    print(f'Para pintar { area }m² será necessário { ceil(refil) } latas e custará R${ ceil(refil * 80) }.')

elif opcCompra == '2':
    refil = area/21.6 # Aqui a mesma coisa de antes só que agora com galões, 3.6 litros(um galão) pinta 21.6 m²(Regra de 3).
    print(f'Para pintar { area }m² será necessário { ceil(refil) } galão(ões) e custará R${ ceil(refil * 25) }.')

elif opcCompra == '3':
    lata = 18
    galao = 3.6
    litros = area / 6 # Vai calcular o total de litros
    litrosExced = litros % lata # Aqui ele vai pegar o resto de uma divisão inteira e vai considerar como litros que sobraram
    print(f'Número de latas uitilizadas são { litros // lata } lata(s) e custará R${ (litros // lata) * 80 }') 
    print(f'Número de galões(ão) uitilizados são { ceil(litrosExced / galao)  } lata(s) e custará R${ ceil(litrosExced / galao) * 25 }')

else:
    print('Comando Invalido')


