# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

paisA = 8000
paisB = 200000
i = 0

while paisA <= paisB:
    i+= 1
    paisA += (paisA * 3)/100
    paisB += (paisB * 1.5)/100

print(f'Ano: {i}, População A: {round(paisA, 2)}, População B: {round(paisB, 2)}')
