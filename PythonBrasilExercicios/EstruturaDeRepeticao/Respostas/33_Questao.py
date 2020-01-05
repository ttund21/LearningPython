# 33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperaturas = []
i = 1

while True:
    try:
        temp = float(input(f'{i}º Temperatura: '))
    except ValueError:
        print('Valor Inválido!')
        continue
    
    i += 1
    temperaturas.append(temp)
   
    parar = input('Quer parar?(sim)\n>>> ')
    if parar == 'sim':
        break
    else:
        continue

print(f'\nMenor temperatura: {min(temperaturas)}\nMaior temperatura: {max(temperaturas)}\nMedia de temperatura: {sum(temperaturas) / len(temperaturas)}')
