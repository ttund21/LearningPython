# 26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

cand1 = 0
cand2 = 0
cand3 = 0

numEle = int(input('Número de eleitores: '))

for i in range(numEle):
    while True:
        eleitor = int(input(f'Eleitor número {i + 1}, vai votar no candidato 1, 2 ou 3?\n>>> '))
        if eleitor == 1:
            cand1 += 1
            break
        elif eleitor == 2:
            cand2 += 1
            break
        elif eleitor == 3:
            cand3 += 1
            break
        else:
            print('Candidato Invalido!')
            continue
        
print(f'\nCandidato 1: {cand1}\nCandidato 2: {cand2}\nCandidato 3: {cand3}')
