# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


from sys import exit
n = []

while True:
    addN = input('Número(Enter para parar): ')
    if addN == '':
        break
    elif float(addN) < 0 or float(addN) > 1000:
        exit('Apenas números entre 0 e 1000')
    else:
        n.append(float(addN))

print(f'Máximo: { max(n) }, Minimo: { min(n) }')
